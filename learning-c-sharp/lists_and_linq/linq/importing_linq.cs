/*
Before we jump into the syntax and methods, let’s import the features into our code. 
To use LINQ in a file, add this line to the top:

using System.Linq;
*/

using System;
using System.Collections.Generic; // Lists
using System.Linq; // LINQ

namespace LearnLinq
{
  class Program
  {
    static void Main()
    {
      List<string> heroes = new List<string> { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
  
      var shortHeroes = from h in heroes
                        where h.Length < 8
                        select h;

      // Printing...
      Console.WriteLine("Your short heroes are...");
      
      foreach (string hero in shortHeroes)
      {
        Console.WriteLine(hero);
      }
    }
  }
}
