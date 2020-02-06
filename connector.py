import openapi_client
from redistimeseries.client import Client
from redis.exceptions import ResponseError
from urllib3.exceptions import MaxRetryError,NewConnectionError
from time import time,sleep,mktime
from datetime import datetime
from confuse import NotFoundError
import os
import logging
import confuse
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
class connector():
    def __init__(self):
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
        
        # Initialize the API client
        self.api_instance=self._init_api()

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
            thread=self.api_instance.get_pods_hist_with_http_info('MK3RxMtR',
            days=self.config['days'].get(int),
            async_req=True)
            HistoricalData, status_code, _=thread.get()
        except MaxRetryError:
            logging.warn('Max Retry Error:{0}'.format(status_code))

        temperature=HistoricalData.result.temperature
        parse_time=lambda datetime_str: int(mktime(datetime.strptime(datetime_str,"%Y-%m-%dT%H:%M:%SZ" ).timetuple()))
        temperature_value,temperature_time=zip(*[[x.value,parse_time(x.time)] for x in temperature])
        return temperature_time,temperature_value

if __name__=="__main__":
    con=connector()
    time,temp =con.pull()
    