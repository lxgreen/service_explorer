namespace ServiceExplorerServer.Model
{
    // Represents request data received from client
    public class RequestData
    {
        // Python naming convention for client compatibility
        public string user_name { get; set; }

        public string ip_address { get; set; }

        public string password { get; set; }
    }
}