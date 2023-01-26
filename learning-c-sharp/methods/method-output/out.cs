/*
A method can only return one value, but sometimes you need to output two pieces 
of information. Calling a method that uses an out parameter is one way to 
return multiple values.
*/

// public static bool TryParse (string s, out int result);

/*
The method returns a boolean and accepts a string and a variable that has been 
declared of type int as input.
*/

using System;

namespace OutParameters
{
  class Program
  {
    static void Main(string[] args)
    {
      string ageAsString = "102";
      string nameAsString = "Granny";

      int ageAsInt = 102;
      bool outcome;
      outcome = Int32.TryParse(ageAsString, out ageAsInt);
      Console.WriteLine(outcome);
      Console.WriteLine(ageAsInt);

      int nameAsInt;
      bool outcome2;
      outcome2 = Int32.TryParse(nameAsString, out nameAsInt);
      Console.WriteLine(outcome2);
      Console.WriteLine(nameAsInt);

    }    
	}
}
