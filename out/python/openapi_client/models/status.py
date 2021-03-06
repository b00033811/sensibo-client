# coding: utf-8

"""
    Sensibo API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Status(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'str',
        'more_results': 'bool',
        'result': 'list[StatusResult]'
    }

    attribute_map = {
        'status': 'status',
        'more_results': 'moreResults',
        'result': 'result'
    }

    def __init__(self, status=None, more_results=None, result=None, local_vars_configuration=None):  # noqa: E501
        """Status - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._more_results = None
        self._result = None
        self.discriminator = None

        self.status = status
        self.more_results = more_results
        self.result = result

    @property
    def status(self):
        """Gets the status of this Status.  # noqa: E501


        :return: The status of this Status.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Status.


        :param status: The status of this Status.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def more_results(self):
        """Gets the more_results of this Status.  # noqa: E501


        :return: The more_results of this Status.  # noqa: E501
        :rtype: bool
        """
        return self._more_results

    @more_results.setter
    def more_results(self, more_results):
        """Sets the more_results of this Status.


        :param more_results: The more_results of this Status.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and more_results is None:  # noqa: E501
            raise ValueError("Invalid value for `more_results`, must not be `None`")  # noqa: E501

        self._more_results = more_results

    @property
    def result(self):
        """Gets the result of this Status.  # noqa: E501


        :return: The result of this Status.  # noqa: E501
        :rtype: list[StatusResult]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Status.


        :param result: The result of this Status.  # noqa: E501
        :type: list[StatusResult]
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Status):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Status):
            return True

        return self.to_dict() != other.to_dict()
