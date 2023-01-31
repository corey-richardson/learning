/*
The from operator declares a variable to iterate through the sequence. In this 
case, h is used to iterate through heroes.

The where operator picks elements from the sequence if they satisfy the given 
condition. The condition is normally written like the conditional expressions 
you would find in an if statement. In this case, the condition is h.Length < 8.

The select operator determines what is returned for each element in the 
sequence. In this case, it’s just the element itself.

The from and select operators are required, where is optional. In this next 
example, select is used to make a new string starting with “Hero: “ for 
each element:

var heroTitles = from hero in heroes
  select $"HERO: {hero.ToUpper()}";
*/

// SELECT FROM WHERE
// -->
// FROM WHERE SELECT

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

      // Write a from - where - select query that selects all of the elements 
      // in heroes that contain the character "i". Store the result in a
      // variable named heroesWithI.
      var heroesWithI = from hero in heroes
        where hero.Contains("i")
        select hero;


      // Write a from - select query that returns the same array as heroes,
      // but every space is replaced with an underscore (_). Store the result
      // in a variable named underscored.
      var underscored = from hero in heroes
        select hero.Replace(" ","_");

      foreach (string hero in heroesWithI)
      { Console.WriteLine(hero); }
      foreach (string us_hero in underscored)
      { Console.WriteLine(us_hero); }

    }
  }
}
