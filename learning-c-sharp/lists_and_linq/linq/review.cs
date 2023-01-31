// There are a few bugs in this code! Fix each one before moving on.

using System;
using System.Collections.Generic;
using System.Linq; // imported linq

namespace LearnLinq
{
  class Program
  {
    static void Main()
    {
      List<string> heroesList = new List<string> 
      { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
      
      // Query syntax
      var queryResult = from h in heroesList // string[] --> var
        where h.Contains("a")
        select $"{h} contains an 'a'";
     
      // Printing...
      Console.WriteLine($"queryResult has {queryResult.Count()} elements";
      // .Count property --> .Count() method
      
      foreach (string s in queryResult)
      {
        Console.WriteLine(s);
      }

      
    }
  }
}
