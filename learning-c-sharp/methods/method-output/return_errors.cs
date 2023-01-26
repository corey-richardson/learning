/*
using System;

namespace ReturnErrors
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine(DecoratePlanet("Mars")); 
      Console.WriteLine("Is Pluto really a dwarf...?");
      Console.WriteLine(IsPlutoADwarf());
      Console.WriteLine("Then how many planets are there in the galaxy...?");
      Console.WriteLine(CountThePlanets());
    }
    
    static DecoratePlanet(string planet)
    {
       return $"*..*..* Welcome to {planet} *..*..*";
    }
    
    static bool IsPlutoADwarf()
    {
      bool answer = true;
    }
    
    static int CountThePlanets()
    {
      return "8 planets, usually";
    }
	}
}
*/

using System;

namespace ReturnErrors
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine(DecoratePlanet("Mars")); 
      Console.WriteLine("Is Pluto really a dwarf...?");
      Console.WriteLine(IsPlutoADwarf()); // true
      Console.WriteLine("Then how many planets are there in the galaxy...?");
      Console.WriteLine(CountThePlanets());
    }
    
    static string DecoratePlanet(string planet)
    {
       return $"*..*..* Welcome to {planet} *..*..*";
    }
    
    static bool IsPlutoADwarf()
    {
      bool answer = true;
      return answer;
    }
    
    static string CountThePlanets()
    {
      return "8 planets, usually";
    }
	}
}
