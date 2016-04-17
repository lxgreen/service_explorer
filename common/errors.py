class InvalidConfigurationError(Exception):
    def __init__(self, message):
        self.message = message

class ServiceExplorerRuntimeError(Exception):
    def __init__(self, message):
        self.message = message