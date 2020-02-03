# coding: utf-8

"""
    Sensibo API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.status_result import StatusResult  # noqa: E501
from openapi_client.rest import ApiException

class TestStatusResult(unittest.TestCase):
    """StatusResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StatusResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.status_result.StatusResult()  # noqa: E501
        if include_optional :
            return StatusResult(
                status = '0', 
                reason = '0', 
                ac_state = openapi_client.models.status_ac_state.status_acState(
                    on = True, 
                    target_temperature = 1.337, 
                    temperature_unit = '0', 
                    mode = '0', 
                    swing = openapi_client.models.swing.swing(), ), 
                changed_properties = [
                    '0'
                    ], 
                id = '0'
            )
        else :
            return StatusResult(
        )

    def testStatusResult(self):
        """Test StatusResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
