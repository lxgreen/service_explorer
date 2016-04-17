import argparse
import sys
from server.data_model import ServerConfiguration
from server.service_explorer_server import ServiceExplorerServer
from common.errors import *


def main():
    # Get port number from command line
    parser = argparse.ArgumentParser(description='Service Explorer Server')
    parser.add_argument('--port', dest='port', type=int, default=8888, help='port number (default: 8888)')
    args = parser.parse_args()
    server = None
    try:
        # Instantiate server
        server_configuration = ServerConfiguration(args.port)
        server = ServiceExplorerServer(server_configuration)
    except InvalidConfigurationError as error:
        print("Error: {0}".format(error.message))
        sys.exit(1)

    # Start server
    if server:
        try:
            server.run()
        except ServiceExplorerRuntimeError as error:
            print("Error: {0}".format(error.message))
            sys.exit(1)

if __name__ == '__main__':
    main()
