# equibles_stocks.FundamentalsApi

All URIs are relative to *https://api.equibles.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dividends**](FundamentalsApi.md#dividends) | **GET** /stocks/fundamentals/dividends | Get the dividends for a given stock.
[**financial_reports**](FundamentalsApi.md#financial_reports) | **GET** /stocks/fundamentals/financialreports | Get the financial statements for a given stock.

# **dividends**
> DividendsResponse dividends(full_ticker, page=page, page_size=page_size)

Get the dividends for a given stock.

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
api_instance = equibles_stocks.FundamentalsApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock. Example: AAPL.XNAS
page = 1 # int | The number of the page to request. Default: 1. (optional) (default to 1)
page_size = 1000 # int | The number of elements in each page. Max value: 1000. Default: 1000. (optional) (default to 1000)

try:
    # Get the dividends for a given stock.
    api_response = api_instance.dividends(full_ticker, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundamentalsApi->dividends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock. Example: AAPL.XNAS | 
 **page** | **int**| The number of the page to request. Default: 1. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 1000. Default: 1000. | [optional] [default to 1000]

### Return type

[**DividendsResponse**](DividendsResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **financial_reports**
> FundamentalsResponse financial_reports(full_ticker, year, fiscal_period, page=page, page_size=page_size)

Get the financial statements for a given stock.

Returns a list of fully qualified ticker names. A fully qualified ticker has the following structure: [Ticker].[ExchangeMic] Example: AAPL.XNAS.

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
api_instance = equibles_stocks.FundamentalsApi(equibles_stocks.ApiClient(configuration))
full_ticker = 'full_ticker_example' # str | The fully qualified ticker of the stock. Example: AAPL.XNAS
year = 56 # int | The year of the report.
fiscal_period = equibles_stocks.FiscalPeriod() # FiscalPeriod | The fiscal period of the report.
page = 1 # int | The number of the page to request. Default: 1. (optional) (default to 1)
page_size = 50 # int | The number of elements in each page. Max value: 50. Default: 50. (optional) (default to 50)

try:
    # Get the financial statements for a given stock.
    api_response = api_instance.financial_reports(full_ticker, year, fiscal_period, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundamentalsApi->financial_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_ticker** | **str**| The fully qualified ticker of the stock. Example: AAPL.XNAS | 
 **year** | **int**| The year of the report. | 
 **fiscal_period** | [**FiscalPeriod**](.md)| The fiscal period of the report. | 
 **page** | **int**| The number of the page to request. Default: 1. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 50. Default: 50. | [optional] [default to 50]

### Return type

[**FundamentalsResponse**](FundamentalsResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

