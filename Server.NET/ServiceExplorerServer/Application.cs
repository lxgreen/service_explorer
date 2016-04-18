using System;
using CommandLine;
using Microsoft.Owin.Hosting;

namespace ServiceExplorerServer
{
    internal class Application
    {
        // Represents the command line options
        private class CLIOptions
        {
            [Option("port", HelpText = "port number (default: 8888)", Required = false)]
            public ushort? PortNumber { get; set; }
        }

        private static void Main(string[] args)
        {
            // Get the port number from command line
            var options = new CLIOptions();
            var port = 8888;
            if (CommandLine.Parser.Default.ParseArguments(args, options))
            {
                port = options.PortNumber ?? 8888;
            }

            var url = string.Format("http://127.0.0.1:{0}/", port);

            // Start server on the selected port
            using (var server = WebApp.Start<Server>(url))
            {
                Console.WriteLine("Server started listening on {0}", url);
                Console.WriteLine("Hit Enter to terminate, any moment\n");
                Console.ReadLine();
            }
        }
    }
}