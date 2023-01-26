// .Length

using System;

namespace ArrayLength
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] summerStrut;

      summerStrut = new string[] { "Juice", "Missing U", "Raspberry Beret", "New York Groove", "Make Me Feel", "Rebel Rebel", "Despacito", "Los Angeles" };

      if (summerStrut.Length == 8)
      {
        Console.WriteLine("summerStrut Playlist is ready to go!");
      }
      else if (summerStrut.Length > 8)
      {
        Console.WriteLine("Too many lines");
      }
      else 
      {
        Console.WriteLine("Add some songs!");
      }
    
    }
  }
}
