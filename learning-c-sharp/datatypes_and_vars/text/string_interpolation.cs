using System;

namespace StoryTime
{
  class Program
  {
    static void Main(string[] args)
    {
      string yourFaveMusician = "King Gizzard and the Lizard Wizard";
      string myFaveMusician = "QOTSA";
      Console.WriteLine($"Your favorite musician is {yourFaveMusician} and mine is {myFaveMusician}.");

      // Declare the variables
      string beginning = "Once upon a time,";
      string middle = "The kid climbed a tree";
      string end = "Everyone lived happily ever after.";

      Console.WriteLine($"{beginning}{middle}. {end}");
    }
  }
}
