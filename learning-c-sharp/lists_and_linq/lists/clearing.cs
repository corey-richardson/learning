using System;
using System.Collections.Generic;

namespace LearnLists
{
  class Program
  {
    static void Main()
    {
      List<double> marathons = new List<double>
      {
        148.22,
        156.10,
        153.88,
        155.34,
        160.89
      };
      
      // Clear the list here
      marathons.Clear();
      
      Console.WriteLine($"Count: {marathons.Count}");
    }
  }
}
