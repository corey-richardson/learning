// This code contains two errors! Delete or comment out the
// lines causing the errors.

using System;

namespace LearnReferences
{
  class Program
  {
    static void Main(string[] args)
    {
      Dissertation diss = new Dissertation();
			IFlippable fdiss = diss;
      Book bdiss = diss;
			fdiss.CurrentPage = 42;
      // bdiss.CurrentPage = 43;
      // fdiss.Stringify();
      bdiss.Stringify();
      Console.WriteLine(fdiss == bdiss);
    }
  }
}
