using System;

namespace BasicClasses
{
  class Program
  {
    static void Main(string[] args)
    {
      Forest f = new Forest("Congo", "Tropical");
      f.Trees = 0;

      // create a Forest object named “Rendlesham”.
      Forest f1 = new Forest("Rendlesham");
      Console.WriteLine(f1.Biome);
      
      Console.WriteLine(f.Name);
      Console.WriteLine(f.Biome);
    }
  }
}
