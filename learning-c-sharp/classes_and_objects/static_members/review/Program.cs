using System;

namespace StaticMembers
{
  class Program
  {
    static void Main(string[] args)
    {
      // From Program.cs, print the number of forests created.
      Console.WriteLine(Forest.ForestsCreated);

      // Instantiate two Forest objects.
      Forest f1 = new Forest("Amazon","Rainforest");
      Forest f2 = new Forest("Congo");

      // Print the number of forests created again.
      Console.WriteLine(Forest.ForestsCreated);
    }
  }
}
