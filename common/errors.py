class InvalidRequestConfigurationError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidClientConfigurationError(Exception):
    def __init__(self, message):
        self.message = message
