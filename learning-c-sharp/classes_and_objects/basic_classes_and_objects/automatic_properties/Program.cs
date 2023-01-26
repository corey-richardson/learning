/*
public string size;
public string Size
{
  get { return size; }
  set { size = value; }
}

-->

public string Size
{ get; set; }
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
      f.age = 0;
      f.biome = "Tropical";
      
      Console.WriteLine(f.Name);
    }
  }
}
