# openapi_client.DefaultApi

All URIs are relative to *https://home.sensibo.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ac_states**](DefaultApi.md#ac_states) | **GET** /pods/{device_id}/acStates | Get AC states
[**get_pods**](DefaultApi.md#get_pods) | **GET** /users/me/pods | Get all devices
[**get_pods_hist**](DefaultApi.md#get_pods_hist) | **GET** /pods/{device_id}/historicalMeasurements | Get Historical data


# **ac_states**
> Status ac_states(device_id, limit=limit)

Get AC states

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Defining host is optional and default to https://home.sensibo.com/api/v2
configuration.host = "https://home.sensibo.com/api/v2"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    device_id = 'device_id_example' # str | device unique id
limit = 'limit_example' # str | number of states to retrieve. Max=20 (optional)

    try:
        # Get AC states
        api_response = api_instance.ac_states(device_id, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->ac_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| device unique id | 
 **limit** | **str**| number of states to retrieve. Max&#x3D;20 | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns when command actually happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pods**
> Pods get_pods(fields=fields)

Get all devices

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Defining host is optional and default to https://home.sensibo.com/api/v2
configuration.host = "https://home.sensibo.com/api/v2"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    fields = 'fields_example' # str | comma separated fields to retrieve or * for all (optional)

    try:
        # Get all devices
        api_response = api_instance.get_pods(fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| comma separated fields to retrieve or * for all | [optional] 

### Return type

[**Pods**](Pods.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pods_hist**
> HistoricalData get_pods_hist(device_id, days=days)

Get Historical data

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Defining host is optional and default to https://home.sensibo.com/api/v2
configuration.host = "https://home.sensibo.com/api/v2"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    device_id = 'device_id_example' # str | device unique id
days = 56 # int | number of days, default is 1 (optional)

    try:
        # Get Historical data
        api_response = api_instance.get_pods_hist(device_id, days=days)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_pods_hist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| device unique id | 
 **days** | **int**| number of days, default is 1 | [optional] 

### Return type

[**HistoricalData**](HistoricalData.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns when command actually happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

