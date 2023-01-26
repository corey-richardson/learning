/*
A bronze coin is worth 1 cent
A silver coin is worth 5 cents
A gold coin is worth 10 cents

16 cents:
16 bronze coins,
3 silver coins and 1 bronze coin, or
1 gold coin, 1 silver coin, 1 bronze coin

*/

using System;

namespace MoneyMaker
{
  class MainClass
  {
    public static void Main(string[] args)
    {
      Console.WriteLine("Welcome to Money Maker!");
      Console.WriteLine("How many cents?");
      int cents = Convert.ToInt32( Console.ReadLine() );
      Console.WriteLine($"{cents} cents is equal to..." );

      int golds = cents / 10;
      cents = cents - (golds * 10);

      int silvers = cents / 5;
      cents = cents - (silvers * 5);

      int bronzes = cents;

      int coins = golds + silvers + bronzes; 

      Console.WriteLine($"Gold coins: {golds}" );
      Console.WriteLine($"Silver coins: {silvers}" );
      Console.WriteLine($"Bronze coins: {bronzes}" );
    }
  }
}

/*
$ dotnet run
Welcome to Money Maker!
How many cents?
17 
17 cents is equal to...
Gold coins: 1
Silver coins: 1
Bronze coins: 2
$ dotnet run
Welcome to Money Maker!
How many cents?
54
54 cents is equal to...
Gold coins: 5
Silver coins: 0
Bronze coins: 4
*/