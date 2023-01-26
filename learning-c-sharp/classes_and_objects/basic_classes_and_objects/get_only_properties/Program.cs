/*
don’t include a set() method, or
make the set() method private.

//This shows approach 1 — don’t include a set():
public string Area
{
  get { return area; }
}

// This shows approach 2 — make set() private:
public int Area
{
  get { return area; }
  private set { area = value; }  
}
*/

using System;

namespace BasicClasses
{
  class Program
  {
    static void Main(string[] args)
    {
      Forest f = new Forest();
      f.Name = "Congo";
      f.Trees = 0;
      // 2. In Program.cs in Main(), try to set the value of f.Age.
      // You should see an error.
      f.Age = 0;
      f.Biome = "Desert";
      
      Console.WriteLine(f.Name);
      Console.WriteLine(f.Biome);
    }
  }
}
