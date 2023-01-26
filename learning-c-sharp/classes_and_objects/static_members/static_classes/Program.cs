// A static class cannot be instantiated, so you only want to do this if you
// are making a utility or library, like Math or Console.

using System;

namespace StaticMembers
{
  class Program
  {
    static void Main(string[] args)
    {
      // We rarely create static classes of our own, so let’s practice using
      // other static classes. 
      // First print the value of pi — a commonly-used value in geometry —,
      // which is stored in Math.PI.
      Console.WriteLine(Math.PI);
      
      // Find the absolute value of -32 using the method Math.Abs(). 
      // This method returns the absolute value, or “positive version”, of 
      // the argument.
      Console.WriteLine(Math.Abs(-32));
    }
  }
}
