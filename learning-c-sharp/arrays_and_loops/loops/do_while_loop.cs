/*
do
{
  statement;
} while (condition);
*/

/*
Instead of checking the condition before the code block executes, the program 
in the block runs once and then checks the conditional statement
*/

/*
Write a program that plays the alarm once, and then if the button isn’t clicked 
(!buttonClick), it will repeat the alarm. To simulate an alarm, you can print 
something like “BLARRRRRRRRR” to the console.
*/

using System;

namespace DoWhileLoop
{
  class Program
  {
    static void Main(string[] args)
    {
      bool buttonClick = true;
      do
      {
        Console.WriteLine("NEE NAW");
      } while (!buttonClick);
      Console.WriteLine("Have a break, have a KitKat.");

    }
  }
}