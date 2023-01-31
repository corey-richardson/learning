/*
As you get into more advanced LINQ queries and learn new operators, you’ll get
a feel for what works best in each situation. For now, we generally follow
these rules:
- For single operator queries, use method syntax.
- For everything else, use query syntax.
*/

/* ```
// Query syntax
var longLoudheroes = from h in heroes
  where h.Length > 6
  select h.ToUpper();

// Method syntax - separate statements
var longHeroes = heroes.Where(h => h.Length > 6);
var longLoudHeroes = longHeroes.Select(h => h.ToUpper());

// Method syntax - chained expressions
var longLoudHeroes2 = heroes
  .Where(h => h.Length > 6)
  .Select(h => h.ToUpper());
``` */

using System;
using System.Collections.Generic;
using System.Linq;

namespace LearnLinq
{
  class Program
  {
    static void Main()
    {
      string[] heroes = 
      { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
      // Write a method-syntax query that transforms each element in heroes 
      // to this format:
      // Introducing...[hero's name]!
      var hero_name = heroes.Select(h => h.Replace(h, $"Introducing...{h}!"));
      foreach (string heroname in hero_name)
      { Console.WriteLine(heroname); }

      // Write a query-syntax query that selects elements containing a space
      // and returns the index of the space in each element. For example,
      // instead of "D. Va", the result should contain 2.
      var hero_idx = from h in heroes
      where h.Contains(" ")
      select h.IndexOf(" ");
      foreach (int idx in hero_idx)
      { Console.WriteLine(idx); }

      
    }
  }
}
