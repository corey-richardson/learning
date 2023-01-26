using System;

namespace OptionalParameters
{
  class Program
  {
    static void Main(string[] args)
    {
      VisitPlanets(3);
      VisitPlanets(4);
      VisitPlanets(5);
      VisitPlanets();
    }
    
    static void VisitPlanets(int numberOfPlanets = 0)
    {
      Console.WriteLine($"You visited {numberOfPlanets} new planets...");
    }
  }
}
