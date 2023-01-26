using System;

namespace BasicClasses
{
  class Program
  {
    static void Main(string[] args)
    {
      Forest f = new Forest();
      f.Name = "Congo";
      f.Trees = 0;
      f.Biome = "Desert";
      
      Console.WriteLine(f.Name);
      Console.WriteLine(f.Biome);
    }
  }
}
