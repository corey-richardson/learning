using System;

namespace LearnReferences
{
  class Program
  {
    static void Main(string[] args)
    {
      Book b1 = new Book();
      Book b2 = b1;

      Console.WriteLine( b1 == b2 );
      // True
      /* The result is true because both variables refer to the same location in memory.

(True is printed even though true is the value. It’s just the compiler formatting for the console.) */
    }
  }
}
