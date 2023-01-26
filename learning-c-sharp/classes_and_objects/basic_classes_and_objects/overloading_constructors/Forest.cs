/*
// Just like other methods, constructors can be overloaded. 
// For example, we may want to define an additional constructor that takes one argument:

public Forest(int area, string country)
{ 
  this.Area = area;
  this.Country = country;
 }
 
public Forest(int area)
{ 
  this.Area = area;
  this.Country = "Unknown";
}

// Now you can create a Forest instance in two ways:

Forest f = new Forest(800, "Hungary");
Forest f2 = new Forest(400);

*/

using System;

namespace BasicClasses
{
  class Forest
  {
    public int age;
    private string biome;
    
    public Forest(string name, string biome)
    {
      this.Name = name;
      this.Biome = biome;
      Age = 0;
    }
    /*
    It should take one parameter, name.
    It should use : this() with the name variable as the first argument   and "Unknown" as the second.
    It should also print a warning to the console about the defaulted value.
*/
    public Forest(string name) : this(name, "Unknown")
    {
      Console.WriteLine("Warning: Default Valued");
    }
    
    public string Name
    { get; set; }
    
    public int Trees
    { get; set; }
    
    public string Biome
    {
      get { return biome; }
      set
      {
        if (value == "Tropical" ||
            value == "Temperate" ||
            value == "Boreal")
        {
          biome = value;
        }
        else
        {
          biome = "Unknown";
        }
      }
    }
    
    public int Age
    { 
      get { return age; }
      private set { age = value; }
    }
     
    public int Grow()
    {
      Trees += 30;
      Age += 1;
      return Trees;
    }
    
    public int Burn()
    {
      Trees -= 20;
      Age += 1;
      return Trees;
    }
    
  }

}
