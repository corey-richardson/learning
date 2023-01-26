/*
using System;

namespace OutErrors
{
  class Program
  {
    static void Main(string[] args)
    {
      string statement = "GARRRR";
      bool marker;
			string murmur = Whisper(statement, marker);
      Console.WriteLine(murmur);
    }  
    
    static string Whisper(string phrase, out bool wasWhisperCalled)
    {
      return phrase.ToLower();
    }
	} 
}
*/

// Fix the first error by using out when calling Whisper().

// Fix the second error by assigning a value to the out parameter 
// wasWhisperCalled in the method body of Whisper().

using System;

namespace OutErrors
{
  class Program
  {
    static void Main(string[] args)
    {
      string statement = "GARRRR";
      bool marker;
			string murmur = Whisper(statement, out marker);
      Console.WriteLine(murmur);
    }  
    
    static string Whisper(string phrase, out bool wasWhisperCalled)
    {
      wasWhisperCalled = true;
      return phrase.ToLower();
    }
	} 
}
