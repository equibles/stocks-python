# equibles_stocks.NewsApi

All URIs are relative to *https://api.equibles.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](NewsApi.md#list) | **GET** /stocks/news/list | Get the latest news for this stock.
[**publishers**](NewsApi.md#publishers) | **GET** /stocks/news/publishers | Get all the available news publishers.

# **list**
> NewsResponse list(full_ticker=full_ticker, publisher_name=publisher_name, page=page, page_size=page_size)

Get the latest news for this stock.

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
api_instance = equibles_stocks.NewsApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock used to filter the results. Example: AAPL.XNAS (optional)
publisher_name = 'publisher_name_example' # str | A news publisher used to filter the results. (optional)
page = 1 # int | The number of the page to request. Default: 1. (optional) (default to 1)
page_size = 100 # int | The number of elements in each page. Max value: 500. Default: 100. (optional) (default to 100)

try:
    # Get the latest news for this stock.
    api_response = api_instance.list(full_ticker=full_ticker, publisher_name=publisher_name, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock used to filter the results. Example: AAPL.XNAS | [optional] 
 **publisher_name** | **str**| A news publisher used to filter the results. | [optional] 
 **page** | **int**| The number of the page to request. Default: 1. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 500. Default: 100. | [optional] [default to 100]

### Return type

[**NewsResponse**](NewsResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers**
> PublishersResponse publishers(page=page, page_size=page_size)

Get all the available news publishers.

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
api_instance = equibles_stocks.NewsApi(equibles_stocks.ApiClient(configuration))
page = 1 # int | The number of the page to request. Default: 1. (optional) (default to 1)
page_size = 100 # int | The number of elements in each page. Max value: 1000. Default: 100. (optional) (default to 100)

try:
    # Get all the available news publishers.
    api_response = api_instance.publishers(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->publishers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the page to request. Default: 1. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 1000. Default: 100. | [optional] [default to 100]

### Return type

[**PublishersResponse**](PublishersResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

