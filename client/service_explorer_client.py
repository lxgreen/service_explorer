import sys
import json
import requests

from client.data_model import ListServicesRequestData, ClientConfiguration
from common.errors import *

# Client
class ServiceExplorerClient:
    # Encapsulates the const Web API info that does not change from request to request.
    # ATM, there is only one request type -- to list all the services.
    _request_settings = {
        "list_services":
            {"url": "/services",
             "method": "get"}
    }

    def __init__(self, client_configuration):
        if not isinstance(client_configuration, ClientConfiguration):
            raise InvalidConfigurationError('invalid client configuration')
        self.configuration = client_configuration

    # "Private" method to request server uniformly
    def _request_server(self, request_data, api_name):
        request_settings = ServiceExplorerClient._request_settings[api_name]
        if request_settings:
            url = ''.join([self.configuration.server_url, request_settings['url']])
            if hasattr(requests, request_settings['method']):
                try:
                    return getattr(requests, request_settings['method'])(url, json=request_data.payload, timeout=20.0)
                # All the possible raised exceptions inherit the RequestException
                except requests.exceptions.RequestException as e:
                    raise ServiceExplorerRuntimeError(e.message)
        return None

    # Public client API
    def list_services(self, request_data):
        if not isinstance(request_data, ListServicesRequestData):
            raise InvalidConfigurationError('invalid request data')

        services = None
        response = self._request_server(request_data, "list_services")
        if response and response.status_code == 200 and response.text != '':
            services = json.loads(response.text)
        elif response.status_code == 500:
            # The Bottle Web Server returns error text in HTML, and it is displayed as is.
            raise ServiceExplorerRuntimeError('{0}. \nError details: {1}'.format(response.reason, response.text))
        return services
