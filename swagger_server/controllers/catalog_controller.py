import connexion
import six

from swagger_server.models.catalog import Catalog  # noqa: E501
from swagger_server import util


def catalog_get(x_broker_api_version):  # noqa: E501
    """get the catalog of services that the service broker offers

     # noqa: E501

    :param x_broker_api_version: version number of the Service Broker API that the Platform will use
    :type x_broker_api_version: str

    :rtype: Catalog
    """
    return 'do some magic!'
