import common.utils as utils
from common.errors import InvalidConfigurationError


# Represents client configuration.
# Validates input, exposes server URL string
class ClientConfiguration:
    MAX_PORT = (1 << 16) - 1

    def __init__(self, server_ip_address, server_port, protocol):
        if not utils.is_valid_ip_address(server_ip_address):
            raise InvalidConfigurationError('invalid server IP address')
        elif server_port <= 0 or server_port > ClientConfiguration.MAX_PORT:
            raise InvalidConfigurationError('invalid server port number')
        elif protocol == "":
            raise InvalidConfigurationError('invalid protocol')
        self.server_url = "{0}://{1}:{2}".format(protocol, server_ip_address, server_port)


# Represents the list services request dynamic data.
# Validates input, exposes a dictionary ready for json serialization
class ListServicesRequestData:
    def __init__(self, user_name, password, ip_address):
        if not utils.is_valid_ip_address(ip_address):
            raise InvalidConfigurationError('invalid IP address')
        elif user_name == "":
            raise InvalidConfigurationError('invalid user name')
        elif password == "":
            raise InvalidConfigurationError('invalid password')
        self.payload = {"user_name": user_name,
                        "password": password,
                        "ip_address": ip_address
                        }
