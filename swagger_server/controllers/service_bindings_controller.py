import connexion
import six

from swagger_server.models.async_operation import AsyncOperation  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.last_operation_resource import LastOperationResource  # noqa: E501
from swagger_server.models.service_binding_request import ServiceBindingRequest  # noqa: E501
from swagger_server.models.service_binding_resource import ServiceBindingResource  # noqa: E501
from swagger_server.models.service_binding_response import ServiceBindingResponse  # noqa: E501
from swagger_server import util


def service_binding_binding(body, x_broker_api_version, instance_id, binding_id, x_broker_api_originating_identity=None, accepts_incomplete=None):  # noqa: E501
    """generate a service binding

     # noqa: E501

    :param body: parameters for the requested service binding
    :type body: dict | bytes
    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: instance id of instance to create a binding on
    :type instance_id: str
    :param binding_id: binding id of binding to create
    :type binding_id: str
    :param x_broker_api_originating_identity: identity of the user that initiated the request from the Platform
    :type x_broker_api_originating_identity: str
    :param accepts_incomplete: asynchronous operations supported
    :type accepts_incomplete: bool

    :rtype: ServiceBindingResponse
    """
    if connexion.request.is_json:
        body = ServiceBindingRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def service_binding_get(x_broker_api_version, instance_id, binding_id, x_broker_api_originating_identity=None, service_id=None, plan_id=None):  # noqa: E501
    """get a service binding

     # noqa: E501

    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: instance id of instance associated with the binding
    :type instance_id: str
    :param binding_id: binding id of binding to fetch
    :type binding_id: str
    :param x_broker_api_originating_identity: identity of the user that initiated the request from the Platform
    :type x_broker_api_originating_identity: str
    :param service_id: id of the service associated with the instance
    :type service_id: str
    :param plan_id: id of the plan associated with the instance
    :type plan_id: str

    :rtype: ServiceBindingResource
    """
    return 'do some magic!'


def service_binding_last_operation_get(x_broker_api_version, instance_id, binding_id, service_id=None, plan_id=None, operation=None):  # noqa: E501
    """get the last requested operation state for service binding

     # noqa: E501

    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: instance id of instance to find last operation applied to it
    :type instance_id: str
    :param binding_id: binding id of service binding to find last operation applied to it
    :type binding_id: str
    :param service_id: id of the service associated with the instance
    :type service_id: str
    :param plan_id: id of the plan associated with the instance
    :type plan_id: str
    :param operation: a provided identifier for the operation
    :type operation: str

    :rtype: LastOperationResource
    """
    return 'do some magic!'


def service_binding_unbinding(x_broker_api_version, instance_id, binding_id, service_id, plan_id, x_broker_api_originating_identity=None, accepts_incomplete=None):  # noqa: E501
    """deprovision a service binding

     # noqa: E501

    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str
    :param instance_id: id of the instance associated with the binding being deleted
    :type instance_id: str
    :param binding_id: id of the binding being deleted
    :type binding_id: str
    :param service_id: id of the service associated with the instance for which a binding is being deleted
    :type service_id: str
    :param plan_id: id of the plan associated with the instance for which a binding is being deleted
    :type plan_id: str
    :param x_broker_api_originating_identity: identity of the user that initiated the request from the Platform
    :type x_broker_api_originating_identity: str
    :param accepts_incomplete: asynchronous operations supported
    :type accepts_incomplete: bool

    :rtype: Object
    """
    return 'do some magic!'
