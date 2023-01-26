using System;

namespace BasicClasses
{
  class Program
  {
    static void Main(string[] args)
    {
      Forest f = new Forest();

      f.name = "New Forest";
      f.biome = "Woodland";
      f.trees = 100;
      f.age = 1;

      Console.WriteLine(f.name);
    }
  }
}
