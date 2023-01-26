using System;

namespace StoryTime
{
  class Program
  {
    static void Main(string[] args)
    {
      string yourFaveMusician = "King Gizzard and the Lizard Wizard";
      string myFaveMusician = "QOTSA";
      Console.WriteLine("Your favorite musician is " + yourFaveMusician + " and mine is " + myFaveMusician + ".");

      //If we want to concatenate a string with something that is another data type, C# will implicitly convert that value to a string.

      // Declare the variables
      string beginning = "Once upon a time, ";
      string middle = "everybody died. ";
      string end = "The end!";
      // Concatenate the string and the variables
      string story = beginning + middle + end;
      // Print the story to the console 
      Console.WriteLine(story);

    }
  }
}
