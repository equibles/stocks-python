# Equibles Stocks API for Python
## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/equibles/stocks-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/equibles/stocks-python.git`)

Then import the package:
```python
import equibles_stocks 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import equibles_stocks
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.equibles.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExchangesApi* | [**currencies**](docs/ExchangesApi.md#currencies) | **GET** /stocks/exchanges/currencies | Get the list of all the currencies supported by this API.
*ExchangesApi* | [**list**](docs/ExchangesApi.md#list) | **GET** /stocks/exchanges/list | Get the list of all the exchanges supported by this API.
*ExchangesApi* | [**stocks**](docs/ExchangesApi.md#stocks) | **GET** /stocks/exchanges/stocks | Get all the stocks for a given exchange.
*FundamentalsApi* | [**dividends**](docs/FundamentalsApi.md#dividends) | **GET** /stocks/fundamentals/dividends | Get the dividends for a given stock.
*FundamentalsApi* | [**financial_reports**](docs/FundamentalsApi.md#financial_reports) | **GET** /stocks/fundamentals/financialreports | Get the financial statements for a given stock.
*MetricsApi* | [**price_to_earnings**](docs/MetricsApi.md#price_to_earnings) | **GET** /stocks/metrics/pricetoearnings | Get the price to earnings ratio over time for this stock.
*NewsApi* | [**list**](docs/NewsApi.md#list) | **GET** /stocks/news/list | Get the latest news for this stock.
*NewsApi* | [**publishers**](docs/NewsApi.md#publishers) | **GET** /stocks/news/publishers | Get all the available news publishers.
*PerformanceApi* | [**list**](docs/PerformanceApi.md#list) | **GET** /stocks/performance/list | Lists the performance for a given stock.
*PricesApi* | [**end_of_day**](docs/PricesApi.md#end_of_day) | **GET** /stocks/prices/endofday | Lists the end of day prices for a given stock.
*PricesApi* | [**intraday**](docs/PricesApi.md#intraday) | **GET** /stocks/prices/intraday | Lists the intraday prices for a given stock with one minute precision.
*SectorsApi* | [**list**](docs/SectorsApi.md#list) | **GET** /stocks/sectors/list | Lists all the sectors.
*SectorsApi* | [**search_stocks**](docs/SectorsApi.md#search_stocks) | **GET** /stocks/sectors/searchstocks | Lists and the stock in a given sector/industry.
*StocksApi* | [**list**](docs/StocksApi.md#list) | **GET** /stocks/list | Get a list of all the available stocks.
*StocksApi* | [**officers**](docs/StocksApi.md#officers) | **GET** /stocks/officers | Get the officers of the company.
*StocksApi* | [**profile**](docs/StocksApi.md#profile) | **GET** /stocks/profile | The profile of this stock.
*StocksApi* | [**screener**](docs/StocksApi.md#screener) | **POST** /stocks/screener | Get a list of stocks constraint to several criteria.
*StocksApi* | [**search**](docs/StocksApi.md#search) | **GET** /stocks/search | Search among all the available stocks.
*StocksApi* | [**splits**](docs/StocksApi.md#splits) | **GET** /stocks/splits | Get all the splits for a given stock.
*TransactionsApi* | [**insiders**](docs/TransactionsApi.md#insiders) | **GET** /stocks/transactions/insiders | Lists the insider transactions for a given stock.
*TransactionsApi* | [**institutional**](docs/TransactionsApi.md#institutional) | **GET** /stocks/transactions/institutional | Lists the institutional transactions for a given stock.

## Documentation For Models

 - [AssetType](docs/AssetType.md)
 - [BalanceSheet](docs/BalanceSheet.md)
 - [CashFlowStatement](docs/CashFlowStatement.md)
 - [CurrenciesResponse](docs/CurrenciesResponse.md)
 - [Currency](docs/Currency.md)
 - [Dividend](docs/Dividend.md)
 - [DividendsResponse](docs/DividendsResponse.md)
 - [Exchange](docs/Exchange.md)
 - [ExchangesResponse](docs/ExchangesResponse.md)
 - [FinancialAssetsResponse](docs/FinancialAssetsResponse.md)
 - [FinancialReport](docs/FinancialReport.md)
 - [FiscalPeriod](docs/FiscalPeriod.md)
 - [FundamentalsResponse](docs/FundamentalsResponse.md)
 - [Image](docs/Image.md)
 - [IncomeStatement](docs/IncomeStatement.md)
 - [Industry](docs/Industry.md)
 - [MetricNullablePointsResponse](docs/MetricNullablePointsResponse.md)
 - [News](docs/News.md)
 - [NewsResponse](docs/NewsResponse.md)
 - [NullablePoint](docs/NullablePoint.md)
 - [Officer](docs/Officer.md)
 - [OfficersResponse](docs/OfficersResponse.md)
 - [Performance](docs/Performance.md)
 - [PerformanceResponse](docs/PerformanceResponse.md)
 - [Price](docs/Price.md)
 - [PricesResponse](docs/PricesResponse.md)
 - [Publisher](docs/Publisher.md)
 - [PublishersResponse](docs/PublishersResponse.md)
 - [Recommendation](docs/Recommendation.md)
 - [ResponseStatus](docs/ResponseStatus.md)
 - [ScreenerRequest](docs/ScreenerRequest.md)
 - [Sector](docs/Sector.md)
 - [SectorsResponse](docs/SectorsResponse.md)
 - [SplitsResponse](docs/SplitsResponse.md)
 - [StockProfile](docs/StockProfile.md)
 - [StockProfileResponse](docs/StockProfileResponse.md)
 - [StockProfilesResponse](docs/StockProfilesResponse.md)
 - [StockSplit](docs/StockSplit.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionType](docs/TransactionType.md)
 - [TransactionsResponse](docs/TransactionsResponse.md)

## Documentation For Authorization

## Query String

- **Type**: API key
- **API key parameter name**: ApiKey
- **Location**: URL query string


## Author
[Equibles](https://www.equibles.com)\
equibles@gmail.com
