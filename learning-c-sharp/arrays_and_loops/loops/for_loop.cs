/*
for (initialization; stopping condition; iteration statement)
{
  statement;
}
*/

/*
for (int i = 0; i < 10; i++)
{
  Console.WriteLine(i);
}
*/

/*
Write an empty for loop that runs once for each week in your 16-week long project
*/

using System;

namespace ForLoop
{
  class Program
  {
    static void Main(string[] args)
    { 
      for(int i = 0; i < 16; i++)
      {
        CreateTemplate(i+1);
      }

    }
    
    static void CreateTemplate(int week)
    {
      Console.WriteLine($"Week {week}");
      Console.WriteLine("Announcements: \n \n \n ");
      Console.WriteLine("Report Backs: \n \n \n");
      Console.WriteLine("Discussion Items: \n \n \n");
    }
    
    
  }
}
