using System;

namespace ServiceExplorerServer.Model
{
    internal class WMIRuntimeError : Exception
    {
        public WMIRuntimeError(string message, Exception inner) : base(message, inner)
        {
        }
    }
}