import argparse
import sys

from client.service_explorer_client import ClientConfiguration, ServiceExplorerClient
from common.errors import InvalidClientConfigurationError, InvalidRequestConfigurationError
from common.data_models import ServiceRequestData

# Get the server ip and port from command line
client = None
parser = argparse.ArgumentParser(description='Service Explorer Console Client')
parser.add_argument('--port', dest='port', type=int, default=8888,
                    help='server port number (default: 8888)')
parser.add_argument('--ip', dest='ip', type=str, default="127.0.0.1",
                    help='server IP address (default: 127.0.0.1)')
args = parser.parse_args()
try:
    config = ClientConfiguration(args.ip, args.port)
    client = ServiceExplorerClient(config)
except InvalidClientConfigurationError as error:
    print("Error: {0}".format(error.message))
    sys.exit(error.message)

if client:
    print("Welcome to Service Explorer Client")
    while True:
        # Get target machine IP, username and password from user
        action = raw_input("\nFor exit, press Q; to continue, hit any other key...")
        if action == "Q" or action == "q":
            print("Bye")
            quit()

        print("Please provide the following details")
        user_name = raw_input("\tUser Name: ")
        password = raw_input("\tPassword: ")
        ip_address = raw_input("\tTarget machine IP address: ")
        try:
            request_data = ServiceRequestData(user_name, password, ip_address)
        except InvalidRequestConfigurationError as error:
            print("Error: {0}".format(error.message))

