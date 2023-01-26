using System;

namespace IfElseStatement
{
  class Program
  {
    static void Main(string[] args)
    {
      int people = 12;
      string weather = "bad";
      if (people <= 10 && weather == "nice")
      {
        Console.WriteLine("SaladMart");
      }
      else
      {
        Console.WriteLine("Soup N Sandwich");
      }

    }
  }
}
