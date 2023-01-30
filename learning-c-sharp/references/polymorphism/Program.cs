// 1. In Program.cs, there are Book type references to one Book and one Diary object. First, call b1.Stringify() and print it to the console.
// 2. Below that call b2.Stringify() and print it to the console.
// To check your understanding, find both Stringify() methods in Diary.cs and Book.cs.

using System;

namespace LearnReferences
{
  class Program
  {
    static void Main(string[] args)
    {
      Book b1 = new Book();
      Book b2 = new Diary();

      Console.WriteLine (b1.Stringify() );
      Console.WriteLine (b2.Stringify() );
      
    }
  }
}
