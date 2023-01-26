using System;

namespace Return
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine(DecoratePlanet("Jupiter"));
    }

    static string DecoratePlanet(string planetName)
    {
      string decoratedName = $"*.*.* Welcome to {planetName} *.*.*";
      
      return decoratedName;
    }
    
	}
}
