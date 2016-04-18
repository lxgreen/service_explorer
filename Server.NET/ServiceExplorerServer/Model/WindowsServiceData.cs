namespace ServiceExplorerServer.Model
{
    // Represents response data sent to client
    public class WindowsServiceData
    {
        // Python naming convention for client compatibility
        public string caption { get; set; }

        public string state { get; set; }

        public string start_mode { get; set; }
    }
}