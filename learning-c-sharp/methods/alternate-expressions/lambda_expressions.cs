// lambda expressions, are great for situations when you need to pass a method as 
// an argument.
// it is an anonymous method: it has no name.

/*
// one expression
(input-parameters) => expression

// more than one expression
(input-parameters) => { statement; }
*/
using System;

namespace AlternateExpressions
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] spaceRocks = {"meteoroid", "meteor", "meteorite"};
      
      // bool makesContact = Array.Exists(spaceRocks, HitGround);
      bool makesContact = Array.Exists(spaceRocks, (string s) => s == "meteorite");
      
      if (makesContact)
      {
        Console.WriteLine("At least one space rock has reached the Earth's surface!");
      } 
    } 
    
    static bool HitGround(string s)
    {
      return s == "meteorite";
    }
  }
}
