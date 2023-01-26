/*
class Forest {
  public int Area
  { // property body omitted  }
  public int IncreaseArea(int growth)
  {
    Area = Area + growth;
    return Area;
  }
}

Forest f = new Forest();
int result = f.IncreaseArea(2);
Console.WriteLine(result); // Prints 2

*/

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

    /////////////////
    public int Grow()
    {
      Trees += 30;
      Age++;
      return Trees;
    }

    public int Burn()
    {
      Trees -= 20;
      Age++;
      return Trees;
    }
    /////////////////
    
  }

}
