using System.Collections.Generic;
using System.Management;

namespace ServiceExplorerServer.Model
{
    internal static class WMIHelper
    {
        // Storage class for const WMI querying data
        private class WMIQueryData
        {
            public string QueryText { get; set; }
            public string Namespace { get; set; }
        }

        // Maps the WMI query data to request key
        // ATM, contains only one entry for GetServices request
        private static readonly Dictionary<string, WMIQueryData> _QueryDataByRequestKey = new Dictionary<string, WMIQueryData>
        {
            { "GetServices", new WMIQueryData { Namespace = @"\root\cimv2", QueryText = "SELECT * FROM Win32_Service" } }
        };

        // Creates connection accordingly to machine IP address, user credentials, and query namespace
        private static ManagementScope GetConnection(string ipAddress, string userName, string password, string @namespace)
        {
            ManagementScope connection = null;

            // Local connection
            if (ipAddress == "127.0.0.1" || ipAddress == Utils.GetLocalIPAddress())
            {
                connection = new ManagementScope();
            }
            else
            {
                var credentials = new ConnectionOptions
                {
                    Username = userName,
                    Password = password
                };

                connection = new ManagementScope(string.Format(@"\\{0}{1}", ipAddress, @namespace), credentials);
            }

            return connection;
        }

        // Queries the WMI uniformly, so the public API can be extended easily
        private static ManagementObjectCollection QueryWMI(RequestData data, string requestKey)
        {
            ManagementObjectCollection result = null;

            WMIQueryData queryData = null;
            if (!_QueryDataByRequestKey.TryGetValue(requestKey, out queryData))
            {
                return result;
            }

            var connection = GetConnection(data.ip_address, data.user_name, data.password, queryData.Namespace);
            if (connection == null)
            {
                return result;
            }

            var serviceQuery = new ObjectQuery(queryData.QueryText);
            var objectSearcher = new ManagementObjectSearcher(connection, serviceQuery);

            result = objectSearcher.Get();

            return result;
        }

        // Public API

        // Returns Services data for given machine and user credentials
        public static IEnumerable<WindowsServiceData> GetServices(RequestData data)
        {
            List<WindowsServiceData> result = null;
            ManagementObjectCollection services = null;
            var requestKey = "GetServices";
            try
            {
                services = QueryWMI(data, requestKey);
            }
            catch (ManagementException ex)
            {
                throw new WMIRuntimeError(requestKey, ex);
            }

            if (services != null)
            {
                result = new List<WindowsServiceData>();

                foreach (var service in services)
                {
                    result.Add(new WindowsServiceData()
                    {
                        caption = service["Caption"].ToString(),
                        start_mode = service["StartMode"].ToString(),
                        state = service["State"].ToString()
                    });
                }
            }

            return result;
        }
    }
}