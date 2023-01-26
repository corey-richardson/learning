using System;

namespace BasicClasses
{
  class Forest
  {
    public int age;
    private string biome;
    
    public string Name
    { get; set; }
    
    public int Trees
    { get; set; }
    
    // 1. In Forest.cs, define an Age property for the age field. 
    // It should have a public getter and a private setter.
    public int Age
    {
      get {return age;}
      private set {age = value;}
    }

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
    
    
  }

}
