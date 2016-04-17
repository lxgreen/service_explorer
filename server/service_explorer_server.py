import json
from bottle import request, route, run, BottleException, abort
from data_model import ServerConfiguration
from common.errors import *
import wmi_helper


@route('/services')
def _list_services():
    body = None
    data = request.json
    if data:
        try:
            services = wmi_helper.get_machine_services(data[u'ip_address'], data[u'user_name'], data[u'password'])
            body = json.dumps(services)
        except Exception as error:
            abort(500, str(error))

    return body


class ServiceExplorerServer:
    def __init__(self, server_configuration):
        if not isinstance(server_configuration, ServerConfiguration):
            raise InvalidConfigurationError('invalid server configuration')
        self.configuration = server_configuration

    def run(self):
        try:
            run(host='localhost', port=self.configuration.port)
        except BottleException as error:
            raise ServiceExplorerRuntimeError(error.message)
