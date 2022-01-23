# equibles_stocks.PerformanceApi

All URIs are relative to *https://api.equibles.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](PerformanceApi.md#list) | **GET** /stocks/performance/list | Lists the performance for a given stock.

# **list**
> PerformanceResponse list(full_ticker)

Lists the performance for a given stock.

### Example
```python
from __future__ import print_function
import time
import equibles_stocks
from equibles_stocks.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = equibles_stocks.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: Query String
configuration = equibles_stocks.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = equibles_stocks.PerformanceApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock. Example: AAPL.XNAS

try:
    # Lists the performance for a given stock.
    api_response = api_instance.list(full_ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock. Example: AAPL.XNAS | 

### Return type

[**PerformanceResponse**](PerformanceResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

