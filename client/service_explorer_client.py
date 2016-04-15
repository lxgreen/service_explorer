import common.utils as utils
from common.errors import InvalidClientConfigurationError

class ClientConfiguration:
    MAX_PORT = (1 << 16) - 1

    def __init__(self, server_ip_address, server_port):
        if not utils.is_valid_ip_address(server_ip_address):
            raise InvalidClientConfigurationError('invalid server IP address')
        elif not server_port or server_port <= 0 or server_port > ClientConfiguration.MAX_PORT:
            raise InvalidClientConfigurationError('invalid server port number')
        self.ip_address = server_ip_address
        self.port = server_port

class ServiceExplorerClient:
    def __init__(self, client_configuration):
        if not client_configuration or not isinstance(client_configuration, ClientConfiguration):
            raise InvalidClientConfigurationError('invalid client configuration')
        self.configuration = client_configuration
