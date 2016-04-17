import common.utils as utils
from common.errors import InvalidConfigurationError


class ServerConfiguration:
    MAX_PORT = (1 << 16) - 1

    def __init__(self, port):
        if port <= 0 or port > ServerConfiguration.MAX_PORT:
            raise InvalidConfigurationError('invalid port number')
        self.port = port
