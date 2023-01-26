using System;

namespace ComparisonOperators
{
  class Program
  {
    static void Main(string[] args)
    {
      double timeToDinner = 4;
      double distance = 95;
      double rate = 30;

      double tripDuration = distance / rate;

      bool answer = tripDuration <= timeToDinner;
      Console.WriteLine(answer);
    }
  }
}
