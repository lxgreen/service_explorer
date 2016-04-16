import wmi
from common.errors import ServiceExplorerRuntimeError


def get_machine_services(ip_address, user_name, password):
    machine = None
    try:
       if ip_address == '127.0.0.1':
           machine = wmi.WMI()
       else:
           machine = wmi.WMI(ip_address, user="{0}\\{1}".format(ip_address, user_name), password=password)
    except wmi.x_wmi as error:
        raise ServiceExplorerRuntimeError(error.message)

    if machine:
        result = []
        try:
            for service in machine.Win32_Service():
                result.append({'caption': service.Caption, 'state': service.State, 'start_mode': service.StartMode})
        except wmi.x_wmi as error:
            raise ServiceExplorerRuntimeError(error.message)
        return result
