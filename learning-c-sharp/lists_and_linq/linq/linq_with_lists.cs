using System;
using System.Collections.Generic;
using System.Linq;

namespace LearnLinq
{
  class Program
  {
    static void Main()
    {
      List<string> heroesList = new List<string> 
      { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };

      // Query heroesList to find all hero names that contain either a '.'
      // or '7' (a period or the number 7).
      var containsPeriodOrSeven = heroesList
      .Where(h => h.Contains(".") || h.Contains("7"));

      foreach(string h in containsPeriodOrSeven)
      { Console.WriteLine(h); }
  
    }
  }
}
