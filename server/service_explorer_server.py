import json
from bottle import request, route, run, BottleException
from data_model import ServerConfiguration
from common.errors import *
import wmi_helper

@route('/services')
def _list_services():
    data = request.json
    if data:
        # print("user: {0}, pass: {1}, ip: {2}".format(data[u'user_name'], data[u'password'], data[u'ip_address']))
        services = wmi_helper.get_machine_services(data[u'ip_address'], data[u'user_name'], data[u'password'])
        return json.dumps(services)

class ServiceExplorerServer:
    def __init__(self, server_configuration):
        if not isinstance(server_configuration, ServerConfiguration):
            raise ServiceExplorerInvalidConfigurationError('invalid server configuration')
        self.configuration = server_configuration

    def run(self):
        try:
            run(host='localhost', port=self.configuration.port)
        except BottleException as error:
            raise ServiceExplorerRuntimeError(error.message)
