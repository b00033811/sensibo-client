import openapi_client
from redistimeseries.client import Client
from redis.exceptions import ResponseError
from urllib3.exceptions import MaxRetryError,NewConnectionError
from openapi_client.exceptions import OpenApiException
from time import time,sleep,mktime
from datetime import datetime
from confuse import NotFoundError
from sys import exit
import os
import logging
import confuse
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
class connector():
    def __init__(self):
        cwd = os.getcwd()
        logging.warn('Current Working Directory: {0}'.format(cwd))
        self.MSEC=1
        self.SEC=self.MSEC*1000
        self.MIN=60*self.SEC
        self.HOUR=60*self.MIN
        self.DAY=24*self.HOUR
        # When deploying this container, connector name must be specified as
        # an enviroment variable in order to pull the configuration
        try:
            if 'CONNECTORNAME' in os.environ:
                logging.info('Connector name: {0}'.format(os.environ['CONNECTORNAME']))
                self.appname=os.environ['CONNECTORNAME']
                self.config=confuse.LazyConfig(self.appname)
                logging.warn('Configuration enviroment loaded\nDetected Keys : {0}'.format(self.config.keys()))
                if self.config.keys()==[]:
                    logging.warn('No keys detected, please ensure that a configmap is configured.')
                    self._debug_config()
            else:
                raise ValueError('Enviroment variable not set: CONNECTORNAME')
        except ValueError as e:
            exit(e)
        # Log File Detection
        filename=self.config['LOG_DIR'].get()
        self.key=self.config['DATABASE_KEY'].get()
        if os.path.exists(filename):
            logging.warn('Log File Detected!')
        # Initialize the API client
        self.api_instance=self._init_api()
        # Intialize Redis Time Series Client
        self.rts=self._init_rts()
        # Create a key if it doesnt exists
        try:
            self.rts.create(self.key,retention_msecs=7*self.DAY)
        except ResponseError as e:
            s = str(e)
            logging.warning(s)
            pass

    def _init_rts(self):
        try:
            #rts = Client(host=os.environ.get('REDIS_HOST'),port=os.environ.get('REDIS_PORT'))
            rts = Client(host=self.config['REDIS_HOST'].get(),port=self.config['REDIS_PORT'].get(),
            decode_responses=True)
        except:
            logging.warning('Failed To initialize Redis client')

        else:
            logging.warning('Redis Client Initialized')
        finally:
            return rts

    def _debug_config(self):
        directory=self.config.config_dir()
        con_file_dir=self.config.user_config_path()
        logging.warn('Config file Directory: {0} | User Config File:{1}'.format(directory,con_file_dir))
    def _init_api(self):
        # Create a sensibo API connector
        configuration = openapi_client.Configuration()
        ############ NEEDS TO BE A SECRET ###############
        configuration.api_key['apiKey'] = 'PCTqTS3UIHDNEMBoH09ScGvMyMvkpQ'
        configuration.host = "https://home.sensibo.com/api/v2"
        api_client= openapi_client.ApiClient(configuration)
        api_instance = openapi_client.DefaultApi(api_client)
        logging.info(os.environ['CONNECTORNAME']+' api client initialized')

        return api_instance
    def pull(self):
        try:
            HistoricalData, _, _=self.api_instance.get_pods_hist_with_http_info('MK3RxMtR',
            days=self.config['days'].get(int))
            temperature=HistoricalData.result.temperature
            parse_time=lambda datetime_str: int(mktime(datetime.strptime(datetime_str,"%Y-%m-%dT%H:%M:%SZ" ).timetuple()))
            temperature_value,temperature_time=zip(*[[x.value,parse_time(x.time)] for x in temperature])
            
        except:
            logging.warn('-----------------------Connection Error-----------------------')
            exit('CRITICAL ERROR')
        finally:
            return temperature_time,temperature_value
    def push(self):
        stream=self.config['STREAM'].get()
        filename=self.config['LOG_DIR'].get()
        if os.path.exists(filename):
            with open(filename,'r') as log:
                # open log file and grab the id of the last messege
                last_line = log.readlines()[-1]
                # query and grab the last timestamp and parse it
                last_record=con.rts.xrevrange(stream,min='-',max=last_line,count=1)
                if last_record==[]:
                    logging.critical('log file exists; last id cannot be recoverd from stream.')
                    exit('critical ERROR')
                last_time=last_record[0][1]['time']
                # pull new data
                time,temp=con.pull()
                #compare new data with previously consumed timestamp
                idx = [i for i,x in enumerate(time) if x>int(last_time)]
                # if the new data has new samples parse it and update the log file
                if idx!=[]:
                    new_time=time[idx[0]::]
                    new_temp=temp[idx[0]::]
                    ID=[con.rts.xadd(stream, dict(temp=x,time=y)) for x,y in zip(new_temp,new_time)]
                    out=[(self.key,time,value) for time,value in zip(time,temp)]
                    self.rts.madd(out)
                    with open(filename, 'a') as log:
                        log.write(os.linesep+ID[-1])
                        logging.warn('Records added: {0}'.format(len(ID)))
                else:
                        logging.warn('No new records')
        # if the log file is missing, create a new one and pull data
        else:
            logging.warn('Could not locate log file, pulling data ...')
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            time,temp =con.pull()
            ID=[con.rts.xadd(stream, dict(temp=x,time=y)) for x,y in zip(temp,time)]
            out=[(self.key,time,value) for time,value in zip(time,temp)]
            self.rts.madd(out)
            with open(filename, 'w') as log:
                log.write(ID[-1])

if __name__=="__main__":
    con=connector()
    import schedule
    import time
    schedule.every(2).minutes.do(con.push)
    while True:
        schedule.run_pending()
        time.sleep(1)