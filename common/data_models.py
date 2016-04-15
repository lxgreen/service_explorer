import utils
from errors import InvalidRequestConfigurationError

class ServiceRequestData:
    def __init__(self, user_name, password, ip_address):
        if not utils.is_valid_ip_address(ip_address):
            raise InvalidRequestConfigurationError('invalid IP address')
        elif user_name == "":
            raise InvalidRequestConfigurationError('invalid user name')
        elif password == "":
            raise InvalidRequestConfigurationError('invalid password')
        self.user_name = user_name
        self.password = password
        self.ip_address = ip_address
