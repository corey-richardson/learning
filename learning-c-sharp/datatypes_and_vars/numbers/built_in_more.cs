// Math.Pow()
// Math.Max()
// Math.Ceiling()

using System;

namespace DocumentationHunt
{
  class Program
  {
    static void Main(string[] args)
    {

      double numberOne = 6.5;
      double numberTwo = 4;

      // Raise numberOne to the numberTwo power
      Console.WriteLine(Math.Pow(numberOne, numberTwo));

      // Round numberOne up
      Console.WriteLine(Math.Ceiling(numberOne));

      // Find the larger number between numberOne and numberTwo
      Console.WriteLine(Math.Max(numberOne, numberTwo));

    }
  }
}
