# equibles_stocks.ExchangesApi

All URIs are relative to *https://api.equibles.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currencies**](ExchangesApi.md#currencies) | **GET** /stocks/exchanges/currencies | Get the list of all the currencies supported by this API.
[**list**](ExchangesApi.md#list) | **GET** /stocks/exchanges/list | Get the list of all the exchanges supported by this API.
[**stocks**](ExchangesApi.md#stocks) | **GET** /stocks/exchanges/stocks | Get all the stocks for a given exchange.

# **currencies**
> CurrenciesResponse currencies()

Get the list of all the currencies supported by this API.

### Example
```python
from __future__ import print_function
import time
import equibles_stocks
from equibles_stocks.rest import ApiException
from pprint import pprint

# Configure API key authorization: Query String
configuration = equibles_stocks.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = equibles_stocks.ExchangesApi(equibles_stocks.ApiClient(configuration))

try:
    # Get the list of all the currencies supported by this API.
    api_response = api_instance.currencies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangesApi->currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrenciesResponse**](CurrenciesResponse.md)

### Authorization

[Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ExchangesResponse list()

Get the list of all the exchanges supported by this API.

### Example
```python
from __future__ import print_function
import time
import equibles_stocks
from equibles_stocks.rest import ApiException
from pprint import pprint

# Configure API key authorization: Query String
configuration = equibles_stocks.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = equibles_stocks.ExchangesApi(equibles_stocks.ApiClient(configuration))

try:
    # Get the list of all the exchanges supported by this API.
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangesApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExchangesResponse**](ExchangesResponse.md)

### Authorization

[Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stocks**
> FinancialAssetsResponse stocks(operating_mic)

Get all the stocks for a given exchange.

Returns a list of fully qualified ticker names. A fully qualified ticker has the following structure: [Ticker].[ExchangeMic] Example: AAPL.XNAS.

### Example
```python
from __future__ import print_function
import time
import equibles_stocks
from equibles_stocks.rest import ApiException
from pprint import pprint

# Configure API key authorization: Query String
configuration = equibles_stocks.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = equibles_stocks.ExchangesApi(equibles_stocks.ApiClient(configuration))
operating_mic = 'operating_mic_example' # str | The operating MIC of the exchange to search.

try:
    # Get all the stocks for a given exchange.
    api_response = api_instance.stocks(operating_mic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangesApi->stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operating_mic** | **str**| The operating MIC of the exchange to search. | 

### Return type

[**FinancialAssetsResponse**](FinancialAssetsResponse.md)

### Authorization

[Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

