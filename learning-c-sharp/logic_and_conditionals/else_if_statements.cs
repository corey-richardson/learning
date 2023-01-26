using System;

namespace ElseIfStatement
{
  class Program
  {
    static void Main(string[] args)
    {
      int guests = 3;
      if (guests >= 4)
      {
        Console.WriteLine("Catan");
      }
      else if (guests >= 1)
      {
        Console.WriteLine("Innovation");
      }
      else
      {
        Console.WriteLine("Solitaire");
      }


    }
  }
}
