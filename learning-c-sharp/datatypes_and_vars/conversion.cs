/*
implicit conversion: happens automatically if no data will be lost in the conversion. 
That’s why it’s possible to convert an int (which can hold less data) to a double 
(which can hold more), but not the other way around.

explicit conversion: requires a cast operator to convert a data type into another 
one. So if we do want to convert a double to an int, we could use the operator (int).
*/

double myDouble = 3.2;
int myInt = myDouble;
// not allowed as data loss happens

double myDouble = 3.2;
int myInt = (int)myDouble;
// explicit conversion overrules data loss block


// Even if that value is an integer or a decimal, Console.ReadLine() will always 
// return a string.

using System;

namespace FavoriteNumber
{
  class Program
  {
    static void Main(string[] args)
    {
      // Ask user for fave number
      Console.Write("Enter your favorite number!: ");

      // int faveNumber = (int)Console.ReadLine();
      /* (int) didn’t work either. That’s because it is not possible to explicitly convert a string into an int (or vice versa) in C#. This time, let’s try using a built-in method to do the conversion. */
      int faveNumber = Convert.ToInt32( Console.ReadLine() );

    }
  }
}
