/*
bool hasEvenNumbers = Array.Exists(numbers, (int num) => num % 2 == 0 );
// num is implicitly int
bool hasEvenNumbers = Array.Exists(numbers, (num) => num % 2 == 0 );
// one parameter in a lambda expression, we don’t need the parentheses around 
// the parameter either
bool hasEvenNumbers = Array.Exists(numbers, num => num % 2 == 0 );

We can remove the parameter type if it can be inferred
We can remove the parentheses if there is one parameter
*/

/*
bool makesContact = Array.Exists(spaceRocks, (string s) => s == "meteorite");
-->
bool makesContact = Array.Exists(spaceRocks, s => s == "meteorite");
*/

using System;

namespace AlternateExpressions
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] spaceRocks = {"meteoroid", "meteor", "meteorite"};
      
      bool makesContact = Array.Exists(spaceRocks, s => s == "meteorite");
      
      if (makesContact)
      {
        Console.WriteLine("At least one space rock has reached the Earth's surface!");
      } 
    } 
  }
}
