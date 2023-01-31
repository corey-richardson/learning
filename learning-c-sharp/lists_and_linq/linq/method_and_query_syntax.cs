/*

Query syntax looks like a multi-line sentence. If you’ve used SQL, you might 
see some similarities:

var longLoudHeroes = from h in heroes
  where h.Length > 6
  select h.ToUpper();

---

Method syntax looks like plain old C#. We make method calls on the collection 
we are querying:

var longHeroes = heroes.Where(h => h.Length > 6);
var longLoudHeroes = longHeroes.Select(h => h.ToUpper());

*/

/* 
Read the two queries in Program.cs. Each one returns a sequence of phrases, 
one for each hero name that contains an ‘a’. Run the code to see the output.

The queries return the same output, but they are written with different syntax. 
Which seems easier to read to you? 
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
      string[] heroes = { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };

      // Query syntax
      var queryResult = from x in heroes
                        where x.Contains("a")
                        select $"{x} contains an 'a'";
      
      // Method syntax
      var methodResult = heroes
        .Where(x => x.Contains("a"))
        .Select(x => $"{x} contains an 'a'");
     
      // Printing...
      Console.WriteLine("queryResult:");
      foreach (string s in queryResult)
      {
        Console.WriteLine(s);
      }
      
      Console.WriteLine("\nmethodResult:");
      foreach (string s in methodResult)
      {
        Console.WriteLine(s);
      }
    }
  }
}
