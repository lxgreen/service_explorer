import wmi
from common.errors import ServiceExplorerRuntimeError


def get_machine_services(ip_address, user_name, password):
    connection = None
    if ip_address == '127.0.0.1':
        connection = wmi.WMI()
    else:
        connection = wmi.WMI(ip_address, user="{0}\\{1}".format(ip_address, user_name), password=password)

    if connection:
        result = []
        for service in connection.Win32_Service():
            result.append({'caption': service.Caption, 'state': service.State, 'start_mode': service.StartMode})

        return result
