using System;

namespace DefineParameters
{
  class Program
  {
    static void Main(string[] args)
    {
      VisitPlanets(3);
      VisitPlanets(0);
      VisitPlanets(9999);
    }
    
    static void VisitPlanets(int numberOfPlanets)
    {
      Console.WriteLine($"You visited {numberOfPlanets} new planets...");
    }
  }
}
