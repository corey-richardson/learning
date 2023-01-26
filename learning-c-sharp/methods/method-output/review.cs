using System;

namespace ReviewMethodOutput
{
  class Program
  {
    static void Main(string[] args)
    {
      // Define variables
      string destination = "Neptune";
      string galaxyString = "8";
      int galaxyInt;
      string welcomeMessage;
      bool outcome;
      
      // Call DecoratePlanet() and TryParse() here
      welcomeMessage = DecoratePlanet(destination);
      outcome = Int32.TryParse(galaxyString, out galaxyInt);

      // Print results
      Console.WriteLine(welcomeMessage);
      Console.WriteLine($"Parsed to int? {outcome}: {galaxyInt}");
      
    }
    
    // Define a method that returns a string
  	static string DecoratePlanet(string planet)
    {
       return $"*..*..* Welcome to {planet} *..*..*";
    }
    
    // Define a method with out
    static string Whisper(string phrase, out bool wasWhisperCalled)
    {
      wasWhisperCalled = true;
      return phrase.ToLower();
    }
	}
}
