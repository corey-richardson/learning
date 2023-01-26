/*
string color = "blue";
string result = (color == "blue") ? "blue" : "NOT blue";
 
Console.WriteLine(result);
*/

// evaluates a single condition and executes one expression if the condition 
// is true and the second expression otherwise.

// type var_name = (expression) ? "true outcome" : "false outcome";

using System;

namespace TernaryOperator
{
  class Program
  {
    static void Main(string[] args)
    {
      int pepperLength = 4;
      // set message to "ready!" if pepperLength >= 3.5, else "wait a little longer"
      string message = (pepperLength >= 3.5) ? "ready!" : "wait a little longer";
      Console.WriteLine(message);


    }
  }
}
