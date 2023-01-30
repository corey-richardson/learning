/*
String, or string, is a class that represents text. Technically its value is 
stored as a collection of char objects.
Since it is a class, it is a reference type. In some cases its behavior looks 
like a value type:
    - A string reference will always point to the original object, so 
    “modifying” one reference to a string will not affect other references.
    - Comparing strings with the equality operator (==) performs a value, not 
    referential, comparison
*/

using System;

namespace StringTheException
{
  class Program
  {
    static void Main(string[] args)
    {
      string var1 = "immutable";
      string var2 = "immutable";

      Console.WriteLine( var1 == var2);
      // True

      Object objVar1 = new Object();
      Object objVar2 = new Object();

      Console.WriteLine( objVar1 == objVar2 );
      // False
      
    }
  }
}
