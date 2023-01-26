using System;

namespace NamedArguments
{
  class Program
  {
    static void Main(string[] args)
    {
      VisitPlanets();
      VisitPlanets(numberOfPlanets: 2);
      VisitPlanets(numberOfPlanets: 2, name: "Corey");
    }
    
    static void VisitPlanets(
      string adjective = "brave",
      string name = "Cosmonaut", 
      int numberOfPlanets = 0,
      double gForce = 4.2)
    {
      Console.WriteLine($"Welcome back, {adjective} {name}.");
      Console.WriteLine($"You visited {numberOfPlanets} new planets...");
      Console.WriteLine($"...while experiencing a g-force of {gForce} g!");
    }
  }
}

/*
Welcome back, brave Cosmonaut.
You visited 0 new planets...
...while experiencing a g-force of 4.2 g!
Welcome back, brave Cosmonaut.
You visited 2 new planets...
...while experiencing a g-force of 4.2 g!
Welcome back, brave Corey.
You visited 2 new planets...
...while experiencing a g-force of 4.2 g!
*/