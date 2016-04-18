using System;
using System.Collections.Generic;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;

namespace ServiceExplorerServer.Model
{
    internal static class Utils
    {
        public static string GetLocalIPAddress()
        {
            try
            {
                List<IPAddress> localIPs = new List<IPAddress>(GetLocalIPAddresses(false));

                if (localIPs.Count == 0)
                {
                    localIPs.AddRange(GetLocalIPAddresses(true));
                }
                if (localIPs.Count == 0)
                {
                    localIPs.AddRange(GetLocalIPAddressesFromDNS());
                }
                if (localIPs.Count > 0)
                {
                    return localIPs[0].ToString();
                }
                else
                {
                    return null;
                }
            }
            catch (Exception)
            {
                return null;
            }
        }

        private static IEnumerable<IPAddress> GetLocalIPAddresses(bool vmIncluded)
        {
            List<IPAddress> localIPs = new List<IPAddress>();

            NetworkInterface[] networkInterfaces = NetworkInterface.GetAllNetworkInterfaces();

            foreach (NetworkInterface networkInterface in networkInterfaces)
            {
                if (networkInterface.OperationalStatus == OperationalStatus.Up) // interface is connected
                {
                    IPInterfaceProperties properties = networkInterface.GetIPProperties();
                    if (properties != null && properties.UnicastAddresses != null)
                    {
                        foreach (UnicastIPAddressInformation info in properties.UnicastAddresses)
                        {
                            if (info.DuplicateAddressDetectionState == DuplicateAddressDetectionState.Preferred && // valid IP
                                info.Address.AddressFamily == AddressFamily.InterNetwork)   // IPv4 only
                            {
                                // Filter out VM network interfaces
                                if (vmIncluded || info.AddressPreferredLifetime != int.MaxValue)
                                {
                                    localIPs.Add(info.Address);
                                }
                            }
                        }
                    }
                }
            }

            return localIPs;
        }

        private static IEnumerable<IPAddress> GetLocalIPAddressesFromDNS()
        {
            List<IPAddress> localIPs = new List<IPAddress>();

            IPHostEntry host = Dns.GetHostEntry(Dns.GetHostName());
            foreach (IPAddress ip in host.AddressList)
            {
                if (ip.AddressFamily == AddressFamily.InterNetwork)
                {
                    localIPs.Add(ip);
                }
            }

            return localIPs;
        }
    }
}