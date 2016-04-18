using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using ServiceExplorerServer.Model;

namespace ServiceExplorerServer.Controllers
{
    public class ServicesController : ApiController
    {
        // GET /services
        public IEnumerable<WindowsServiceData> Get([FromBody] RequestData data)
        {
            Console.WriteLine("GET /services request received");
            Console.WriteLine(string.Format("Data: user_name = {0}, password = {1}, ip_address = {2}",
                data.user_name, data.password, data.ip_address));

            IEnumerable<WindowsServiceData> response = null;

            try
            {
                response = WMIHelper.GetServices(data);
                Console.WriteLine(string.Format("Response: ready"));
            }
            catch (WMIRuntimeError error)
            {
                throw new HttpResponseException(new HttpResponseMessage
                {
                    StatusCode = HttpStatusCode.InternalServerError,
                    ReasonPhrase = error.InnerException.Message
                });
            }
            return response;
        }
    }
}