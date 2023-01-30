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
        144.07,
        143.12,
        146.73,
        146.33
      };

      List<double> topMarathons = marathons.GetRange(0,3);

      int i = 1;
      foreach (double time in topMarathons)
      {
        Console.WriteLine($"{i}. {time}");
        i++;
      }

    }
  }
}
