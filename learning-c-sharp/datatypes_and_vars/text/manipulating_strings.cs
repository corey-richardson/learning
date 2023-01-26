using System;

namespace MovieScript
{
  class Program
  {
    static void Main(string[] args)
    {
      // Script line
      string script = "Close on a portrait of the HANDSOME PRINCE -- as the BEAST'S giant paw slashes it.";

      // Get camera directions
      int charPosition = script.IndexOf("Close");
      int length = "Close on".Length;
      string cameraDirections = script.Substring(charPosition, length);

      // Get scene description
      charPosition = script.IndexOf("a portrait");
      string sceneDescription = script.Substring(charPosition);

      // Make camera directions uppercase
      string cameraDirections = cameraDirections.ToUpper();

      // Make scene description lowercase
      string sceneDescription = sceneDescription.ToLower();

      // Print results
      Console.WriteLine(cameraDirections);
      Console.WriteLine(sceneDescription);
    }
  }
}
