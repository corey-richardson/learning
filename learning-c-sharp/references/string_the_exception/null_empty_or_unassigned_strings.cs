// Strings can be Null or Empty or Unassigned
/*
unassigned means that the programmer did not give the variable any value

null means that the programmer intentionally made the variable refer to no object

an empty string signifies a piece of text with zero characters. This is often 
used to represent a blank text field. It can be represented by "" or String.Empty
*/

// The Microsoft Programming Guide suggests using String.Empty or "" instead of 
// null to avoid NullReferenceException errors.

using System;

namespace StringTheException
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Input: ");
      string user_input = Console.ReadLine();

      if (String.IsNullOrEmpty(user_input) )
      { 
        Console.WriteLine("You didn't enter anything!"); 
      }
      else
      {
        Console.WriteLine("Thank you for your submission!");
      }
    }
  }
}

/*
$ dotnet run
Input: 
hello 
Thank you for your submission!
$ dotnet run
Input: 

You didn't enter anything!
*/