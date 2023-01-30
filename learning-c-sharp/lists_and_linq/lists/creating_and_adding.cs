using System;
using System.Collections.Generic;

namespace LearnLists
{
  class Program
  {
    static void Main()
    {
      // Create a list to hold the top women’s marathon times in minutes.
      // Create an empty list of type double and store it in a variable marathons. 
      List<double> marathons = new List<double>();
      // Use two Add() statements to add those values to the list.
      marathons.Add(144.07);
      marathons.Add(143.12);
      // Print the second value in the list to the console.
      Console.WriteLine(marathons[1]);
    }
  }
}
