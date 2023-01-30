/*
To remove a specific item from a list we use the Remove() method. It expects the specific item as an argument and it returns true if it was successfully removed. This code removes "Delhi" from the list and returns true.
If the specific item does NOT exist in the list, the method call returns false. Since "Dubai" isn’t in the list, success will be false:
*/
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

      Console.WriteLine(marathons[1]);
      
      bool removed = marathons.Remove(143.12);

      Console.WriteLine(marathons[1]);
      Console.WriteLine(removed);
      

    }
  }
}
