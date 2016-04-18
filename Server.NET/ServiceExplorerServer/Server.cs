using System;
using System.Net.Http.Formatting;
using System.Web.Http;
using Owin;

namespace ServiceExplorerServer
{
    public class Server
    {
        // Called by the framework on WebApp.Start
        public void Configuration(IAppBuilder appBuilder)
        {
            var serverConfiguration = new HttpConfiguration();

            // Set JSON response format
            serverConfiguration.Formatters.JsonFormatter.MediaTypeMappings.Add(
                new RequestHeaderMapping("Accept", "text/html", StringComparison.InvariantCultureIgnoreCase, true, "application/json"));

            // Route mapping for /services
            serverConfiguration.Routes.MapHttpRoute(name: "Services", routeTemplate: "{controller}");
            appBuilder.UseWebApi(serverConfiguration);
        }
    }
}