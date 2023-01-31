/*
The where operator is written as the method Where(), which takes a lambda 
expression as an argument. Remember that lambda expressions are a quick way to 
write a method. In this case, the method returns true if h is less than 8 
characters long.
*/

// string[] heroes = { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
// var shortHeroes = heroes.Where(h => h.Length < 8);

// [ D. Va, Lucio, Mercy, Pharah ]

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
      // Write a method-syntax query that selects all of the elements in heroes
      // containing the character "i". Store the result in a variable named
      // heroesWithI.
      var heroesWithI = heroes.Where( h => h.Contains("i"));

      foreach (string hero in heroesWithI)
      { Console.WriteLine(hero); }
      
    }
  }
}
