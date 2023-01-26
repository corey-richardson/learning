/*
// zero indexed

int[] plantHeights = {3, 4, 6};
 
// plantTwoHeight will be 4
int plantTwoHeight = plantHeights[1];

*/

using System;

namespace AccessingArrays
{
  class Program
  {
    static void Main(string[] args)
    {     
      string[] summerStrut;
      
      summerStrut = new string[] { "Juice", "Missing U", "Raspberry Beret", "New York Groove", "Make Me Feel", "Rebel Rebel", "Despacito", "Los Angeles" };
      
      int[] ratings = { 5, 4, 4, 3, 3, 5, 5, 4 };
      
      Console.WriteLine($"You rated the song {summerStrut[1]} {ratings[1]} stars.");
    }
  }
}
