# Service Explorer Server .NET

## Description
The project goal is to create service that exposes RESTful API to retrieve all the Windows Services for given machine.

## Implementation details
The server is powered by the ASP.NET Web API component. To simplify deployment, it uses [OWIN](http://owin.org/) SelfHost package that allows to integrate the Web API into a console application rather than to host it on IIS.

The service consists of the following components:

* `Application` contains the entry point that just starts the `Server`.
* `Server` configures the Web API routing and response format
* `Controllers` folder contains the only Controller for `/services` request
* `Model` folder contains all the necessary helpers, request/response data models, exceptions, and utils

According to the requirements, the Server exposes a single API `/services`, and returns the Service list in JSON format.