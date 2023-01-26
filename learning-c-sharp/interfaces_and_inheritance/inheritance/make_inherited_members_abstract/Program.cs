using System;

namespace LearnInheritance
{
  class Program
  {
    static void Main(string[] args)
    {
      Sedan s = new Sedan(60);
      
      Truck t = new Truck(45, 500);
      
      Bicycle b = new Bicycle(10);

      // 3. In Program.cs, call Describe on each instance and print the result to the console.
      Console.WriteLine(s.Describe());
      Console.WriteLine(t.Describe());
      Console.WriteLine(b.Describe());
    }
  }
}