// string[] heroes = 
// { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
// var loudHeroes = heroes.Select(h => h.ToUpper());

/* We can combine Select() with Where() in two ways: 

Use separate statements:

var longHeroes = heroes.Where(h => h.Length > 6);
var longLoudHeroes = longHeroes.Select(h => h.ToUpper());

Chain the expressions:

var longLoudHeroes = heroes
.Where(h => h.Length > 6)
.Select(h => h.ToUpper());
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
      string[] heroes = 
      { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
      // Selects all of the elements in heroes containing the character "c" and
      // Transforms them to lowercase

      // SEPERATE
      var contains_c = heroes.Where(h => h.Contains("c"));
      var lowerHeroesWithC = contains_c.Select(h => h.ToLower());

      // CHAINED
      var sameResult = heroes
      .Where(h => h.Contains("c"))
      .Select(h => h.ToLower());

      foreach(string hero in lowerHeroesWithC)
      { Console.WriteLine($"Seperate: {hero}"); }
      foreach(string hero in sameResult)
      { Console.WriteLine($"Chained: {hero}"); }


      
    }
  }
}
