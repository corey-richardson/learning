/*
Instantiate a new object with the name "Amazon". Store the result in a variable.
Print the Trees property to the console.
Call the Grow() method.
Print the Trees property again to the console to confirm that the Grow() method works.
*/

using System;

namespace BasicClasses
{
  class Program
  {
    static void Main(string[] args)
    {
      Forest amzn = new Forest("Amazon");
      Console.WriteLine(amzn.Trees);
      amzn.Grow();
      Console.WriteLine(amzn.Trees);
    }
  }
}
