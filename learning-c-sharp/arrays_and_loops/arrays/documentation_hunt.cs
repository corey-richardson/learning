using System;

namespace DocumentationHunt
{
  class Program
  {
    static void Main(string[] args)
    {     
      string[] summerStrut;
      
      summerStrut = new string[] { "Juice", "Missing U", "Raspberry Beret", "New York Groove", "Make Me Feel", "Rebel Rebel", "Despacito", "Los Angeles" };
      
      int[] ratings = { 5, 4, 4, 3, 3, 5, 5, 4 };

      // Array.Copy(Array src, Array dst, int length);
      // init empty array of length 8
      string[] summerStrutCopy = new string[8];
      Array.Copy(summerStrut, summerStrutCopy, 8);

      Console.WriteLine(summerStrut[0]);
      Console.WriteLine(summerStrut[7]);
      Array.Reverse(summerStrut);
      Console.WriteLine(summerStrut[7]);
      Console.WriteLine(summerStrut[0]);

                              // range 0-end
      Array.Clear(summerStrut, 0, summerStrut.Length);
      Console.WriteLine(summerStrut[0]);

    }
  }
}
