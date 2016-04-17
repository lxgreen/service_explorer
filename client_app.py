import argparse
import sys

from tabulate import tabulate
from client.data_model import ListServicesRequestData, ClientConfiguration
from client.service_explorer_client import ServiceExplorerClient
from common.errors import *


def main():
    client = None
    # Get the server ip, protocol, and port from command line
    parser = argparse.ArgumentParser(description='Service Explorer Console Client')
    parser.add_argument('--port', dest='port', type=int, default=8888,
                        help='server port number (default: 8888)')
    parser.add_argument('--ip', dest='ip', type=str, default="127.0.0.1",
                        help='server IP address (default: 127.0.0.1)')
    parser.add_argument('--protocol', dest='protocol', type=str, default="http",
                        help='communication protocol (default: http)')
    args = parser.parse_args()
    try:
        config = ClientConfiguration(args.ip, args.port, args.protocol)
        client = ServiceExplorerClient(config)
    except InvalidConfigurationError as error:
        print("Error: {0}".format(error.message))
        sys.exit(error.message)

    if client:
        print("Welcome to Service Explorer Client")
        print("Server URL: {0}".format(client.configuration.server_url))
        print("Client encoding: {0}".format(sys.stdout.encoding))
        while True:
            action = raw_input("\nSelect an action:\n"
                               "   L    list machine Windows Services\n"
                               "   Q    quit\n")
            if action == "Q" or action == "q":
                print('Bye')
                sys.exit(0)
            elif action == "L" or action == "l":
                # Get target machine IP, username and password from user
                print("Please provide the following details")
                user_name = raw_input("\tUser Name: ")
                password = raw_input("\tPassword: ")
                ip_address = raw_input("\tTarget machine IP address: ")
                request_data = None
                try:
                    request_data = ListServicesRequestData(user_name, password, ip_address)
                except InvalidConfigurationError as error:
                    print("Error: {0}".format(error.message))

                if request_data:
                    services = None
                    try:
                        services = client.list_services(request_data)
                    except ServiceExplorerRuntimeError as error:
                        print("Error: {0}".format(error.message))

                    if services:
                        # Pretty output result, considering the console encoding
                        print tabulate(services,
                                       headers={"caption": "SERVICE CAPTION", "start_mode": "START MODE",
                                                "state": "STATE"}).encode(sys.stdout.encoding, errors='replace')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Bye')
        sys.exit(0)
