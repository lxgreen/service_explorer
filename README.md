# Service Explorer

## Description
The main project goal is to create service that exposes RESTful API to retrieve all the Windows Services for given machine, and a console client that uses this service and displays results to user.

### Server
The server is powered by Bottle Web framework that allows to implement RESTful APIs easily.
The server backend is based on wmi module for Service querying.

According to requirements, the server exposes a single API `/services`, and returns the Service list in JSON format.

### Client
The client is a simple console application that prompts user to enter the required information: IP address of the target machine and user credentials for authentication.
The client sends the provided data in JSON format within GET request to `/services` API.

## Configuration
Both client and server are configured by command line arguments.

The server configuration consists of single parameter -- port number to listen on. By default, the server listens on port 8888.

The client configuration includes three parameters: server IP address, port number, and the communication protocol. The default values are `127.0.0.1`, `8888`, and `http`, respectively.

The exact configuration syntax is available by running the client/server with `--help` key.

## Dependencies
The project is implemented in Python 2.7.9.

In addition to Python standard library, the project relies on the following 3rd party dependencies.

Server dependencies:
* bottle -- Web framework for Web server implementation and request routing
* WMI -- for querying the Windows machines
* pywin32 -- WMI dependency

Client dependencies:
* ipaddress -- IP address validation
* requests -- Web requests to server
* tabulate -- pretty console output

The exact versions are available in `requirements.txt` file.





