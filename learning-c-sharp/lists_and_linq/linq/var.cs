/*
var is just an implicitly typed variable — we let the C# compiler determine 
the actual type for us. Here’s one example:
*/

using System;
using System.Collections.Generic;
using System.Linq;

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

      foreach (string shortHero in shortHeroes)
      {
        Console.WriteLine(shortHero);
      }
      Console.WriteLine(shortHeroes.Count());

      Console.WriteLine("---");

      var longHeroes = heroes.Where(n => n.Length > 8);
      foreach (string longHero in longHeroes)
      { Console.WriteLine(longHero); }
      Console.WriteLine(longHeroes.Count());
      
      
    }
  }
}
