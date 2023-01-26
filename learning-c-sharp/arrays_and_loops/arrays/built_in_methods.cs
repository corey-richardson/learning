// Array.Sort()
// Array.IndexOf()
// Array.Find()

using System;

namespace BuiltInMethods
{
  class Program
  {
    static void Main(string[] args)
    {     
      string[] summerStrut;
      
      summerStrut = new string[] { "Juice", "Missing U", "Raspberry Beret", "New York Groove", "Make Me Feel", "Rebel Rebel", "Despacito", "Los Angeles" };
      
      int[] ratings = { 5, 4, 4, 3, 3, 5, 5, 4 };

      // IndexOf
      Console.WriteLine($"Song number {Array.IndexOf(ratings, 3)+1} is rated three stars");

      // Find
      Console.WriteLine($"The first song that has more than 10 characters in the title is {Array.Find(summerStrut, song => song.Length > 10)}");

      // Sort
      Array.Sort(summerStrut);
      Console.WriteLine(summerStrut[0]);
      Console.WriteLine(summerStrut[7]);

    }
  }
}
