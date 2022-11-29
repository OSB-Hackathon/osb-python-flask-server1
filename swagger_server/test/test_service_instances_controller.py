# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.async_operation import AsyncOperation  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.last_operation_resource import LastOperationResource  # noqa: E501
from swagger_server.models.service_instance_async_operation import ServiceInstanceAsyncOperation  # noqa: E501
from swagger_server.models.service_instance_provision_request_body import ServiceInstanceProvisionRequestBody  # noqa: E501
from swagger_server.models.service_instance_provision_response import ServiceInstanceProvisionResponse  # noqa: E501
from swagger_server.models.service_instance_resource import ServiceInstanceResource  # noqa: E501
from swagger_server.models.service_instance_update_request_body import ServiceInstanceUpdateRequestBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestServiceInstancesController(BaseTestCase):
    """ServiceInstancesController integration test stubs"""

    def test_service_instance_deprovision(self):
        """Test case for service_instance_deprovision

        deprovision a service instance
        """
        query_string = [('service_id', 'service_id_example'),
                        ('plan_id', 'plan_id_example'),
                        ('accepts_incomplete', true)]
        headers = [('x_broker_api_version', '2.13'),
                   ('x_broker_api_originating_identity', 'x_broker_api_originating_identity_example')]
        response = self.client.open(
            '/v2/service_instances/{instance_id}'.format(instance_id='instance_id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_service_instance_get(self):
        """Test case for service_instance_get

        get a service instance
        """
        query_string = [('service_id', 'service_id_example'),
                        ('plan_id', 'plan_id_example')]
        headers = [('x_broker_api_version', '2.13'),
                   ('x_broker_api_originating_identity', 'x_broker_api_originating_identity_example')]
        response = self.client.open(
            '/v2/service_instances/{instance_id}'.format(instance_id='instance_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_service_instance_last_operation_get(self):
        """Test case for service_instance_last_operation_get

        get the last requested operation state for service instance
        """
        query_string = [('service_id', 'service_id_example'),
                        ('plan_id', 'plan_id_example'),
                        ('operation', 'operation_example')]
        headers = [('x_broker_api_version', '2.13')]
        response = self.client.open(
            '/v2/service_instances/{instance_id}/last_operation'.format(instance_id='instance_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_service_instance_provision(self):
        """Test case for service_instance_provision

        provision a service instance
        """
        body = ServiceInstanceProvisionRequestBody()
        query_string = [('accepts_incomplete', true)]
        headers = [('x_broker_api_version', '2.13'),
                   ('x_broker_api_originating_identity', 'x_broker_api_originating_identity_example')]
        response = self.client.open(
            '/v2/service_instances/{instance_id}'.format(instance_id='instance_id_example'),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_service_instance_update(self):
        """Test case for service_instance_update

        update a service instance
        """
        body = ServiceInstanceUpdateRequestBody()
        query_string = [('accepts_incomplete', true)]
        headers = [('x_broker_api_version', '2.13'),
                   ('x_broker_api_originating_identity', 'x_broker_api_originating_identity_example')]
        response = self.client.open(
            '/v2/service_instances/{instance_id}'.format(instance_id='instance_id_example'),
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
