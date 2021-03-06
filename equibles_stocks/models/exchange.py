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

class Exchange(object):
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
        'name': 'str',
        'asset_type': 'AssetType',
        'operating_mic': 'str',
        'country': 'str',
        'currency_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'asset_type': 'assetType',
        'operating_mic': 'operatingMic',
        'country': 'country',
        'currency_code': 'currencyCode'
    }

    def __init__(self, name=None, asset_type=None, operating_mic=None, country=None, currency_code=None):  # noqa: E501
        """Exchange - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._asset_type = None
        self._operating_mic = None
        self._country = None
        self._currency_code = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if asset_type is not None:
            self.asset_type = asset_type
        if operating_mic is not None:
            self.operating_mic = operating_mic
        if country is not None:
            self.country = country
        if currency_code is not None:
            self.currency_code = currency_code

    @property
    def name(self):
        """Gets the name of this Exchange.  # noqa: E501


        :return: The name of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Exchange.


        :param name: The name of this Exchange.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def asset_type(self):
        """Gets the asset_type of this Exchange.  # noqa: E501


        :return: The asset_type of this Exchange.  # noqa: E501
        :rtype: AssetType
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this Exchange.


        :param asset_type: The asset_type of this Exchange.  # noqa: E501
        :type: AssetType
        """

        self._asset_type = asset_type

    @property
    def operating_mic(self):
        """Gets the operating_mic of this Exchange.  # noqa: E501


        :return: The operating_mic of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._operating_mic

    @operating_mic.setter
    def operating_mic(self, operating_mic):
        """Sets the operating_mic of this Exchange.


        :param operating_mic: The operating_mic of this Exchange.  # noqa: E501
        :type: str
        """

        self._operating_mic = operating_mic

    @property
    def country(self):
        """Gets the country of this Exchange.  # noqa: E501


        :return: The country of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Exchange.


        :param country: The country of this Exchange.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def currency_code(self):
        """Gets the currency_code of this Exchange.  # noqa: E501


        :return: The currency_code of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Exchange.


        :param currency_code: The currency_code of this Exchange.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

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
        if issubclass(Exchange, dict):
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
        if not isinstance(other, Exchange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
