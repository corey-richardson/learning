using System;

namespace CallAMethod
{
  class Program
  {
    static void Main(string[] args)
    {
      string msg = "Yabba dabba doo!";
      Math.Min(1,2);
      Console.WriteLine(msg);
      Console.WriteLine(msg.Substring(0,1));
    }
  }
}
