using System;

namespace TheObjectClass
{
  class Program
  {
    static void Main(string[] args)
    {
      Diary dairy = new Diary(1, "Me", "My Dairy Log (A Beginners Guide to Lactose)");
      // Let’s prove to ourselves that ToString() is used 
      // when printing to the console.
      Console.WriteLine( dairy );
    }
  }
}
