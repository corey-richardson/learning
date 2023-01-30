using System;

namespace StringTheException
{
  class Program
  {
    static void Main(string[] args)
    {
      string lyrics = 
        "Dollie, Dollie, bo-bollie,\n" +
        "Banana-fana fo-follie\n" +
        "Fee-fi-mo-mollie\n" +
        "Dollie!";
      
      // Call `Replace()` here
      lyrics = lyrics.Replace("ollie","ana");
      
      Console.WriteLine(lyrics);
    }
  }
}
