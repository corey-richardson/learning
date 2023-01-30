/*
Create a variable of type Book and set it to null.

Print the variable to the console.
Remember that null presents a null reference, so you should see nothing printed.

Compare the variable to null using the == operator and print the result to the console.
*/

using System;

namespace LearnReferences
{
  class Program
  {
    static void Main(string[] args)
    {
      Book null_book = null;
      Console.WriteLine(null_book);
      Console.WriteLine(null_book == null);
    }
  }
}
