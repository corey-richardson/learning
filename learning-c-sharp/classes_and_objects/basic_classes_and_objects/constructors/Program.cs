using System;

namespace BasicClasses
{
  class Program
  {
    static void Main(string[] args)
    {
      // Forest f = new Forest(); --> parameterkess constructor, error
      // Forest(string, string) has been defined.
      
      Forest f = new Forest("Congo", "Tropical");
      f.Trees = 0;
      
      Console.WriteLine(f.Name);
      Console.WriteLine(f.Biome);
    }
  }
}
