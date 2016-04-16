import common.utils as utils
from common.errors import ServiceExplorerInvalidConfigurationError

class ServerConfiguration:
    MAX_PORT = (1 << 16) - 1

    def __init__(self, port):
        if port <= 0 or port > ServerConfiguration.MAX_PORT:
            raise ServiceExplorerInvalidConfigurationError('invalid port number')
        self.port = port