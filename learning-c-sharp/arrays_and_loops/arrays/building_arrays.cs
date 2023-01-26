/*

// These arrays store ints, strings, and doubles, respectively
int[] x; 
string[] s; 
double[] d; 

int[] plantHeights = { 3, 4, 6 };
int[] plantHeights = new int[] { 3, 4, 6 };

// Initial declaration
int[] plantHeights;
// This works
plantHeights = new int[] { 3, 4, 6 };   
// This will cause an error
// plantHeights = { 3, 4, 6 }; 

*/

using System;

namespace BuildingArrays
{
  class Program
  {
    static void Main(string[] args)
    {
      //  declare a string array called summerStrut. 
      // This will be the playlist that we add our songs to.
      string[] summerStrut;
      // On a new line, initialize your array with eight song 
      // titles as values.
      summerStrut = new string[] {"Southern Nights",
      "Here Comes the Sun",
      "Everybody's Gotta Live",
      "We Are Never Getting Back Together",
      "happier",
      "Split",
      "The Chain",
      "Life on Mars?"};

      int[] ratings = {4,3,4,3,5,5,3,4};

      
    }
  }
}
