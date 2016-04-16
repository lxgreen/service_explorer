import ipaddress

def is_valid_ip_address(ip_address):
    try:
        parsed = ipaddress.ip_address(unicode(ip_address))
        return parsed is not None
    except ValueError:
        return False
