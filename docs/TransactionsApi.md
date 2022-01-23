# equibles_stocks.TransactionsApi

All URIs are relative to *https://api.equibles.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insiders**](TransactionsApi.md#insiders) | **GET** /stocks/transactions/insiders | Lists the insider transactions for a given stock.
[**institutional**](TransactionsApi.md#institutional) | **GET** /stocks/transactions/institutional | Lists the institutional transactions for a given stock.

# **insiders**
> TransactionsResponse insiders(full_ticker, page=page, page_size=page_size)

Lists the insider transactions for a given stock.

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
api_instance = equibles_stocks.TransactionsApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock. Example: AAPL.XNAS
page = 1 # int | The number of the page to request. Default: 1. (optional) (default to 1)
page_size = 1000 # int | The number of elements in each page. Max value: 1000. Default: 1000. (optional) (default to 1000)

try:
    # Lists the insider transactions for a given stock.
    api_response = api_instance.insiders(full_ticker, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->insiders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock. Example: AAPL.XNAS | 
 **page** | **int**| The number of the page to request. Default: 1. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 1000. Default: 1000. | [optional] [default to 1000]

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **institutional**
> TransactionsResponse institutional(full_ticker, page=page, page_size=page_size)

Lists the institutional transactions for a given stock.

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
api_instance = equibles_stocks.TransactionsApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock. Example: AAPL.XNAS
page = 1 # int | The number of the page to request. Default: 1. (optional) (default to 1)
page_size = 1000 # int | The number of elements in each page. Max value: 1000. Default: 1000. (optional) (default to 1000)

try:
    # Lists the institutional transactions for a given stock.
    api_response = api_instance.institutional(full_ticker, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->institutional: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock. Example: AAPL.XNAS | 
 **page** | **int**| The number of the page to request. Default: 1. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 1000. Default: 1000. | [optional] [default to 1000]

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

