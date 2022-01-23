# equibles_stocks.SectorsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SectorsApi.md#list) | **GET** /stocks/sectors/list | Lists all the sectors.
[**search_stocks**](SectorsApi.md#search_stocks) | **GET** /stocks/sectors/searchstocks | Lists and the stock in a given sector/industry.

# **list**
> SectorsResponse list()

Lists all the sectors.

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
api_instance = equibles_stocks.SectorsApi(equibles_stocks.ApiClient(configuration))

try:
    # Lists all the sectors.
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorsApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SectorsResponse**](SectorsResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_stocks**
> FinancialAssetsResponse search_stocks(sector_name=sector_name, industry_name=industry_name)

Lists and the stock in a given sector/industry.

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
api_instance = equibles_stocks.SectorsApi(equibles_stocks.ApiClient(configuration))
sector_name = 'sector_name_example' # str | The name of the sector to use as filter. (optional)
industry_name = 'industry_name_example' # str | The name of the industry to use as filter. (optional)

try:
    # Lists and the stock in a given sector/industry.
    api_response = api_instance.search_stocks(sector_name=sector_name, industry_name=industry_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorsApi->search_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sector_name** | **str**| The name of the sector to use as filter. | [optional] 
 **industry_name** | **str**| The name of the industry to use as filter. | [optional] 

### Return type

[**FinancialAssetsResponse**](FinancialAssetsResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

