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
  class Forest
  {
    public int age;
    public string biome;
    
    public string Name
    { get; set; }
    
    public int Trees
    {get; set;}
    
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
