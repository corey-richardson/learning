/*
foreach (type element in sequence)
{
  statement;
}
*/

// similar to 'for i in list' loop in python

/*
string[] melody = { "a", "b", "c", "c", "b" };

foreach (string note in melody)
{
  PlayMusic(note);
}
*/

/*
Write an empty loop that will iterate through each item in your todo array.
Inside of the loop, call the CreateTodoItem() method.
*/

using System;

namespace ForEachLoop
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] todo = { "respond to email", "make wireframe", "program feature", "fix bugs" };
      foreach (string task in todo)
      {
        CreateTodoItem(task);
      }

    }
    
    static void CreateTodoItem(string item)
    {
      Console.WriteLine($"[] {item}");
    }
  }
}
