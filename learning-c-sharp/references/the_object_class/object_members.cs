using System;

namespace TheObjectClass
{
  class Program
  {
    static void Main(string[] args)
    {
      Book b = new Book();      
      Diary d = new Diary(38);
      Random r = new Random();
      int i = 9;

      Object[] checkpoint_1 = {b, d, r, i};

      foreach (Object checkpoint_2 in checkpoint_1){
        Console.WriteLine($"Checkpoint 3: {checkpoint_2.GetType()}");
      }
    }
  }
}