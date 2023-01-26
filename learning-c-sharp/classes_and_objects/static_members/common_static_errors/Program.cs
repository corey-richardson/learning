using System;

namespace StaticMembers
{
  class Program
  {
    static void Main(string[] args)
    {
      Forest f = new Forest("Congo", "Tropical");
      
      f.Grow();
      
      Console.WriteLine(Forest.TreeFacts);
    }
  }
}
