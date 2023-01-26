/*
Each time we run dotnet run, the Main() method is called. We can include 
arguments on the command line, like dotnet run arg1 arg2 arg3 that will 
be converted into an array as the args parameter. In the console, enter:

dotnet run mango pineapple lychee

*/

using System;

namespace ApplyingClasses
{
  class Program
  {
    static void Main(string[] args)
    {
      if (args.Length > 0)
      {
        string mainPhrase = String.Join(" and ", args);
        Console.WriteLine($"My favorite fruits are {mainPhrase}!");
      }
    }
  } 
}

/* OUTPUT
$ dotnet run mango pineapple lychee
My favorite fruits are mango and pineapple and lychee!
*/