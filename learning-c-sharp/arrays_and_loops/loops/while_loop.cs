/*
while (condition) 
{
  statement;
}
*/

/*
Write a while loop that checks to see if there are any emails in your inbox. 
If there are still emails, decrease the amount of emails by one until there 
are no emails left.
*/

using System;

namespace WhileLoop
{
  class Program
  {
    static void Main(string[] args)
    {
      int emails = 20;  
      while (emails > 0)
      {
        Console.WriteLine("Deleting email...");
        emails--;
        Console.WriteLine($"Remaining: {emails}\n");
      }
      Console.WriteLine("Emails cleared!");
    }
  }
}
