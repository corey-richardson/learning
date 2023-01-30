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
      
      //   double futureWinner = marathons[-1];
      //   marathons[4] = 143.23;
      double futureWinner = marathons[1];
      marathons[3] = 143.23;
      
      Console.WriteLine("If you reached this point, there are no errors!");
    }
  }
}
