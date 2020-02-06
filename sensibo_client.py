
import openapi_client
from redistimeseries.client import Client
from redis.exceptions import ResponseError
from time import time,sleep,mktime
from datetime import datetime
import os
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
#Time Definitions for Redis
MSEC=1
SEC=MSEC*1000
MIN=60*SEC
HOUR=60*MIN
DAY=24*HOUR
# Create a sensibo API connector
configuration = openapi_client.Configuration()
configuration.api_key['apiKey'] = 'PCTqTS3UIHDNEMBoH09ScGvMyMvkpQ'
configuration.host = "https://home.sensibo.com/api/v2"
api_client= openapi_client.ApiClient(configuration)
# Initialize the instance and get historical data 
api_instance = openapi_client.DefaultApi(api_client)

def pull():
    response=api_instance.get_pods_hist('MK3RxMtR',days=7)
    temperature=response.result.temperature
    parse_time=lambda datetime_str: int(mktime(datetime.strptime(datetime_str,"%Y-%m-%dT%H:%M:%SZ" ).timetuple()))
    temperature_value,temperature_time=zip(*[[x.value,parse_time(x.time)] for x in temperature])
    return temperature_time,temperature_value
#Initialize Redis Client
try:
    #rts = Client(host=os.environ.get('REDIS_HOST'),port=os.environ.get('REDIS_PORT'))
    rts = Client(host='localhost',port=6379)
except:
    logging.warning('Could not connect to redis server')
key='Temperature'

# Create a key if it doesnt exists
try:
    rts.create(key,retention_msecs=DAY)
except ResponseError as e:
    s = str(e)
    print(s)
    pass


while(True):
    try:
        temperature_time,temperature_value=pull()
    except ResponseError:
        logging.warning('Failed to Pull data')
    out=[(key,time,value) for time,value in zip(temperature_time,temperature_value)]
    t=rts.madd(out)
    logging.warning('key inserted with last timestamp: {0}'.format(t[-1]))
    sleep(60*2)
