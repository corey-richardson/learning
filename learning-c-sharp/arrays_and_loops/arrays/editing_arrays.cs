using System;

namespace EditingArrays
{
  class Program
  {
    static void Main(string[] args)
    {     
      string[] summerStrut;
      
      summerStrut = new string[] { "Juice", "Missing U", "Raspberry Beret", "New York Groove", "Make Me Feel", "Rebel Rebel", "Despacito", "Los Angeles" };
      int[] ratings = { 5, 4, 4, 3, 3, 5, 5, 4 };

      summerStrut[7] = "I Like It";
      ratings[7] = 1;
      
      Console.WriteLine(summerStrut[7]); Console.WriteLine(ratings[7]);
      // i hate that that works        ^
    }
  }
}
