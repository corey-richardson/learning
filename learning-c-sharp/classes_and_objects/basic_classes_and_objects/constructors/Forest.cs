/*
In each of the examples so far, we created a new Forest object and set 
the property values one by one. It would be nice if we could write a 
method that’s run every time an object is created to set those values at
once.
*/
/*
name, which sets the Name property
biome, which sets the Biome property
It should also set the value of Age to 0.
*/

using System;

namespace BasicClasses
{
  class Forest
  {

    public int age;
    private string biome;
    
    // constructor
    public Forest(string name, string biome)
    {
      Name = name;
      Biome = biome;
      Age = 0;
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
