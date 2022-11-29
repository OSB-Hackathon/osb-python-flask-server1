import connexion
import six

from swagger_server.models.async_operation import AsyncOperation  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.last_operation_resource import LastOperationResource  # noqa: E501
from swagger_server.models.service_instance_async_operation import ServiceInstanceAsyncOperation  # noqa: E501
from swagger_server.models.service_instance_provision_request_body import ServiceInstanceProvisionRequestBody  # noqa: E501
from swagger_server.models.service_instance_provision_response import ServiceInstanceProvisionResponse  # noqa: E501
from swagger_server.models.service_instance_resource import ServiceInstanceResource  # noqa: E501
from swagger_server.models.service_instance_update_request_body import ServiceInstanceUpdateRequestBody  # noqa: E501
from swagger_server import util


def service_instance_deprovision(x_broker_api_version, instance_id, service_id, plan_id, x_broker_api_originating_identity=None, accepts_incomplete=None):  # noqa: E501
    """deprovision a service instance

     # noqa: E501

    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: id of instance being deleted
    :type instance_id: str
    :param service_id: id of the service associated with the instance being deleted
    :type service_id: str
    :param plan_id: id of the plan associated with the instance being deleted
    :type plan_id: str
    :param x_broker_api_originating_identity: identity of the user that initiated the request from the Platform
    :type x_broker_api_originating_identity: str
    :param accepts_incomplete: asynchronous deprovision supported
    :type accepts_incomplete: bool

    :rtype: Object
    """
    return 'do some magic!'


def service_instance_get(x_broker_api_version, instance_id, x_broker_api_originating_identity=None, service_id=None, plan_id=None):  # noqa: E501
    """get a service instance

     # noqa: E501

    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: instance id of instance to fetch
    :type instance_id: str
    :param x_broker_api_originating_identity: identity of the user that initiated the request from the Platform
    :type x_broker_api_originating_identity: str
    :param service_id: id of the service associated with the instance
    :type service_id: str
    :param plan_id: id of the plan associated with the instance
    :type plan_id: str

    :rtype: ServiceInstanceResource
    """
    return 'do some magic!'


def service_instance_last_operation_get(x_broker_api_version, instance_id, service_id=None, plan_id=None, operation=None):  # noqa: E501
    """get the last requested operation state for service instance

     # noqa: E501

    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: instance id of instance to find last operation applied to it
    :type instance_id: str
    :param service_id: id of the service associated with the instance
    :type service_id: str
    :param plan_id: id of the plan associated with the instance
    :type plan_id: str
    :param operation: a provided identifier for the operation
    :type operation: str

    :rtype: LastOperationResource
    """
    return 'do some magic!'


def service_instance_provision(body, x_broker_api_version, instance_id, x_broker_api_originating_identity=None, accepts_incomplete=None):  # noqa: E501
    """provision a service instance

     # noqa: E501

    :param body: parameters for the requested service instance provision
    :type body: dict | bytes
    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: instance id of instance to provision
    :type instance_id: str
    :param x_broker_api_originating_identity: identity of the user that initiated the request from the Platform
    :type x_broker_api_originating_identity: str
    :param accepts_incomplete: asynchronous operations supported
    :type accepts_incomplete: bool

    :rtype: ServiceInstanceProvisionResponse
    """
    if connexion.request.is_json:
        body = ServiceInstanceProvisionRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def service_instance_update(body, x_broker_api_version, instance_id, x_broker_api_originating_identity=None, accepts_incomplete=None):  # noqa: E501
    """update a service instance

     # noqa: E501

    :param body: parameters for the requested service instance update
    :type body: dict | bytes
    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: instance id of instance to update
    :type instance_id: str
    :param x_broker_api_originating_identity: identity of the user that initiated the request from the Platform
    :type x_broker_api_originating_identity: str
    :param accepts_incomplete: asynchronous operations supported
    :type accepts_incomplete: bool

    :rtype: Object
    """
    if connexion.request.is_json:
        body = ServiceInstanceUpdateRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
