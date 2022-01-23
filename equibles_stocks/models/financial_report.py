# coding: utf-8

"""
    Stocks

    <h3>Authentication</h3>                     You need to authenticate to use this API.                     To authenticate click on the \"Authorize\" button and do one of the following steps.<br />                     1. Send your API key in the headers of the request by typing \"Bearer my-key\" on the Bearer authorization scheme.<br />                     2. Send your API key on the \"ApiKey\" query string parameter. To do this type your API key in the Query String authorization scheme.<br />                     Both methods are equally valid. We offer both options so that you can use the method that is easier to use in your application.<br />                     <br />                     <h3>API limits</h3>                     Your API key may be subject to daily/hourly limits. To know how much requests you have left look at the following headers in the response.<br />                     1. <strong>x-ratelimit-limit</strong> - The total number of requests that you are allowed to make in a given period (hour/day)                       2. <strong>x-ratelimit-remaining</strong> - The number of remaining requests that you can perform in the current period.<br />                     3. <strong>x-ratelimit-reset</strong> - The number of seconds until the current period resets.<br />                     <br />                     <h3>Suggestions</h3>                     You don't need to implement the whole API by hand in your programming language of choice.<br />                     Since this API has an OpenAPI specification you can use                      <a href=\"https://github.com/swagger-api/swagger-codegen\" target=\"_blank\">Swagger Generator</a>                      to automatically generate client stubs for more than 30 programming languages.                     <br />                     <br />                     You don't have an API key? <a href=\"https://www.equibles.com/api/pricing\" target=\"_blank\">Get one for free here.</a>  # noqa: E501

    OpenAPI spec version: v1
    Contact: equibles@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FinancialReport(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'balance_sheet': 'BalanceSheet',
        'cash_flow_statement': 'CashFlowStatement',
        'income_statement': 'IncomeStatement',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'fiscal_period': 'FiscalPeriod',
        'year': 'int'
    }

    attribute_map = {
        'balance_sheet': 'balanceSheet',
        'cash_flow_statement': 'cashFlowStatement',
        'income_statement': 'incomeStatement',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'fiscal_period': 'fiscalPeriod',
        'year': 'year'
    }

    def __init__(self, balance_sheet=None, cash_flow_statement=None, income_statement=None, start_date=None, end_date=None, fiscal_period=None, year=None):  # noqa: E501
        """FinancialReport - a model defined in Swagger"""  # noqa: E501
        self._balance_sheet = None
        self._cash_flow_statement = None
        self._income_statement = None
        self._start_date = None
        self._end_date = None
        self._fiscal_period = None
        self._year = None
        self.discriminator = None
        if balance_sheet is not None:
            self.balance_sheet = balance_sheet
        if cash_flow_statement is not None:
            self.cash_flow_statement = cash_flow_statement
        if income_statement is not None:
            self.income_statement = income_statement
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if fiscal_period is not None:
            self.fiscal_period = fiscal_period
        if year is not None:
            self.year = year

    @property
    def balance_sheet(self):
        """Gets the balance_sheet of this FinancialReport.  # noqa: E501


        :return: The balance_sheet of this FinancialReport.  # noqa: E501
        :rtype: BalanceSheet
        """
        return self._balance_sheet

    @balance_sheet.setter
    def balance_sheet(self, balance_sheet):
        """Sets the balance_sheet of this FinancialReport.


        :param balance_sheet: The balance_sheet of this FinancialReport.  # noqa: E501
        :type: BalanceSheet
        """

        self._balance_sheet = balance_sheet

    @property
    def cash_flow_statement(self):
        """Gets the cash_flow_statement of this FinancialReport.  # noqa: E501


        :return: The cash_flow_statement of this FinancialReport.  # noqa: E501
        :rtype: CashFlowStatement
        """
        return self._cash_flow_statement

    @cash_flow_statement.setter
    def cash_flow_statement(self, cash_flow_statement):
        """Sets the cash_flow_statement of this FinancialReport.


        :param cash_flow_statement: The cash_flow_statement of this FinancialReport.  # noqa: E501
        :type: CashFlowStatement
        """

        self._cash_flow_statement = cash_flow_statement

    @property
    def income_statement(self):
        """Gets the income_statement of this FinancialReport.  # noqa: E501


        :return: The income_statement of this FinancialReport.  # noqa: E501
        :rtype: IncomeStatement
        """
        return self._income_statement

    @income_statement.setter
    def income_statement(self, income_statement):
        """Sets the income_statement of this FinancialReport.


        :param income_statement: The income_statement of this FinancialReport.  # noqa: E501
        :type: IncomeStatement
        """

        self._income_statement = income_statement

    @property
    def start_date(self):
        """Gets the start_date of this FinancialReport.  # noqa: E501


        :return: The start_date of this FinancialReport.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FinancialReport.


        :param start_date: The start_date of this FinancialReport.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this FinancialReport.  # noqa: E501


        :return: The end_date of this FinancialReport.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this FinancialReport.


        :param end_date: The end_date of this FinancialReport.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def fiscal_period(self):
        """Gets the fiscal_period of this FinancialReport.  # noqa: E501


        :return: The fiscal_period of this FinancialReport.  # noqa: E501
        :rtype: FiscalPeriod
        """
        return self._fiscal_period

    @fiscal_period.setter
    def fiscal_period(self, fiscal_period):
        """Sets the fiscal_period of this FinancialReport.


        :param fiscal_period: The fiscal_period of this FinancialReport.  # noqa: E501
        :type: FiscalPeriod
        """

        self._fiscal_period = fiscal_period

    @property
    def year(self):
        """Gets the year of this FinancialReport.  # noqa: E501


        :return: The year of this FinancialReport.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this FinancialReport.


        :param year: The year of this FinancialReport.  # noqa: E501
        :type: int
        """

        self._year = year

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FinancialReport, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FinancialReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
