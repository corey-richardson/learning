/*
AddRange() — takes an array or list as an argument. Adds the values to the end 
of the list. Returns nothing.

InsertRange() — takes an int and array or list as an argument. Adds the values 
at the int index. Returns nothing.

RemoveRange() — takes two int values. The first int is the index at which to 
begin removing and the second int is the number of elements to remove. 
Returns nothing.

GetRange() — takes two int values. The first int is the index of the first 
desired element and the second int is the number of elements in the desired 
range. Returns a list of the same type.
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
