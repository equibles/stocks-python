# equibles_stocks.StocksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](StocksApi.md#list) | **GET** /stocks/list | Get a list of all the available stocks.
[**officers**](StocksApi.md#officers) | **GET** /stocks/officers | Get the officers of the company.
[**profile**](StocksApi.md#profile) | **GET** /stocks/profile | The profile of this stock.
[**search**](StocksApi.md#search) | **GET** /stocks/search | Search among all the available stocks.
[**splits**](StocksApi.md#splits) | **GET** /stocks/splits | Get all the splits for a given stock.

# **list**
> CommonStocksResponse list(page=page, page_size=page_size)

Get a list of all the available stocks.

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
api_instance = equibles_stocks.StocksApi(equibles_stocks.ApiClient(configuration))
page = 1 # int |  (optional) (default to 1)
page_size = 100 # int |  (optional) (default to 100)

try:
    # Get a list of all the available stocks.
    api_response = api_instance.list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StocksApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**CommonStocksResponse**](CommonStocksResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **officers**
> OfficersResponse officers(full_ticker)

Get the officers of the company.

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
api_instance = equibles_stocks.StocksApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock. Example: AAPL.XNAS

try:
    # Get the officers of the company.
    api_response = api_instance.officers(full_ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StocksApi->officers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock. Example: AAPL.XNAS | 

### Return type

[**OfficersResponse**](OfficersResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile**
> CommonStockResponse profile(full_ticker)

The profile of this stock.

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
api_instance = equibles_stocks.StocksApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock. Example: AAPL.XNAS

try:
    # The profile of this stock.
    api_response = api_instance.profile(full_ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StocksApi->profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock. Example: AAPL.XNAS | 

### Return type

[**CommonStockResponse**](CommonStockResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> CommonStocksResponse search(text, page=page, page_size=page_size)

Search among all the available stocks.

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
api_instance = equibles_stocks.StocksApi(equibles_stocks.ApiClient(configuration))
text = 'text_example' # str | The text to search for.
page = 1 # int |  (optional) (default to 1)
page_size = 100 # int |  (optional) (default to 100)

try:
    # Search among all the available stocks.
    api_response = api_instance.search(text, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StocksApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to search for. | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**CommonStocksResponse**](CommonStocksResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **splits**
> SplitsResponse splits(full_ticker, page=page, page_size=page_size)

Get all the splits for a given stock.

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
api_instance = equibles_stocks.StocksApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock. Example: AAPL.XNAS
page = 1 # int |  (optional) (default to 1)
page_size = 1000 # int |  (optional) (default to 1000)

try:
    # Get all the splits for a given stock.
    api_response = api_instance.splits(full_ticker, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StocksApi->splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock. Example: AAPL.XNAS | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 1000]

### Return type

[**SplitsResponse**](SplitsResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

