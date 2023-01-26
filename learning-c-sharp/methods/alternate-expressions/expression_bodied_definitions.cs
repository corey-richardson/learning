/*
bool IsEven(int num)
{
  return num % 2 == 0;
}

bool isEven(int num) => num % 2 == 0;
*/

/*
static double DaysToRotations(double days)
{
    return days / 365;
}
*/

/*
static void Welcome(string planet)
{
    Console.WriteLine($"Welcome to {planet}!");
}
*/

using System;

namespace AlternateExpressions
{
  class Program
  {
    static void Main(string[] args)
    {
      Welcome("Earth");
      double days = 500;
      double rotations = DaysToRotations(days);
      Console.WriteLine($"In {days} days, the Earth has rotated {rotations} time(s).");
    }

    static double DaysToRotations(double days) => days / 365;
    static void Welcome(string planet) => Console.WriteLine($"Welcome to {planet}!");
    
  }
}
