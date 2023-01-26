/*
while loops are good when you know your stopping condition, but not when you 
know how many times you want a program to loop or if you have a specific 
collection to loop through.

do...while loops are only necessary if you definitely want something to run 
once, but then stop if a condition is met.

for loops are best if you want something to run a specific number of times, 
rather than given a certain condition.

foreach loops are the best way to loop over an array, or any other collection.
*/

using System;

namespace ComparingLoops
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] websites = { "twitter", "facebook", "gmail" };
      
      // Re-write the loop so that it uses a loop that better suits the 
      // objective.
      /*
      int counter = 0;
      while (counter < websites.Length)
      { 
        Console.WriteLine(websites[counter]); 
        counter++; 
      }
      */

      foreach (string site in websites)
      {
        Console.WriteLine(site);
      }

    }
  }
}
