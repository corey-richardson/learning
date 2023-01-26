/*
string color;
 
switch (color)
{
   case "blue":
      // execute if the value of color is "blue"
      Console.WriteLine("color is blue");
      break;
   case "red":
      // execute if the value of color is "red"
      Console.WriteLine("color is red");
      break;
   case "green":
      // execute if the value of color is "green"
      Console.WriteLine("color is green");
      break;
   default:
      // execute if none of the above conditions are met
      break;
}
*/

using System;

namespace SwitchStatement
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Genre: ");
      string genre = Console.ReadLine();
      switch (genre)
      {
        case "Drama":
          Console.WriteLine("Citizen Kane");
          break;
        case "Comedy":
          Console.WriteLine("Duck Soup");
          break;
        case "Adventure":
          Console.WriteLine("king Kong");
          break;
        case "Horror":
          Console.WriteLine("Psycho");
          break;
        case "Science Fiction":
          Console.WriteLine("2001: A Space Odyssey");
          break;
        default:
          Console.WriteLine("No movie found");
          break;
      }

    }
  }
}
