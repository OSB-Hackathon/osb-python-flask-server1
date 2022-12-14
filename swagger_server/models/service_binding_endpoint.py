# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ServiceBindingEndpoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, host: str=None, ports: List[str]=None, protocol: str='tcp'):  # noqa: E501
        """ServiceBindingEndpoint - a model defined in Swagger

        :param host: The host of this ServiceBindingEndpoint.  # noqa: E501
        :type host: str
        :param ports: The ports of this ServiceBindingEndpoint.  # noqa: E501
        :type ports: List[str]
        :param protocol: The protocol of this ServiceBindingEndpoint.  # noqa: E501
        :type protocol: str
        """
        self.swagger_types = {
            'host': str,
            'ports': List[str],
            'protocol': str
        }

        self.attribute_map = {
            'host': 'host',
            'ports': 'ports',
            'protocol': 'protocol'
        }
        self._host = host
        self._ports = ports
        self._protocol = protocol

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceBindingEndpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceBindingEndpoint of this ServiceBindingEndpoint.  # noqa: E501
        :rtype: ServiceBindingEndpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host(self) -> str:
        """Gets the host of this ServiceBindingEndpoint.


        :return: The host of this ServiceBindingEndpoint.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this ServiceBindingEndpoint.


        :param host: The host of this ServiceBindingEndpoint.
        :type host: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def ports(self) -> List[str]:
        """Gets the ports of this ServiceBindingEndpoint.


        :return: The ports of this ServiceBindingEndpoint.
        :rtype: List[str]
        """
        return self._ports

    @ports.setter
    def ports(self, ports: List[str]):
        """Sets the ports of this ServiceBindingEndpoint.


        :param ports: The ports of this ServiceBindingEndpoint.
        :type ports: List[str]
        """
        if ports is None:
            raise ValueError("Invalid value for `ports`, must not be `None`")  # noqa: E501

        self._ports = ports

    @property
    def protocol(self) -> str:
        """Gets the protocol of this ServiceBindingEndpoint.


        :return: The protocol of this ServiceBindingEndpoint.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol: str):
        """Sets the protocol of this ServiceBindingEndpoint.


        :param protocol: The protocol of this ServiceBindingEndpoint.
        :type protocol: str
        """
        allowed_values = ["tcp", "udp", "all"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"
                .format(protocol, allowed_values)
            )

        self._protocol = protocol
