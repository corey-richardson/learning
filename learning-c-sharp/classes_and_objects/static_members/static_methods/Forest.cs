using System;

namespace StaticMembers
{
  class Forest
  {
    // FIELDS
    
    public int age;
    private string biome;
    private static int forestsCreated;
    // Define a private static string field named treeFacts.
    private static string treeFacts;
    
    // CONSTRUCTORS
    
    public Forest(string name, string biome)
    {
      this.Name = name;
      this.Biome = biome;
      Age = 0;
      ForestsCreated++;
    }
    
    public Forest(string name) : this(name, "Unknown")
    { }
    
    // PROPERTIES
    
    // Define a public static property named TreeFacts with just a getter (no setter).
    public static string TreeFacts
    {
      get { return treeFacts; }
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
    
    public static int ForestsCreated
    {
      get { return forestsCreated; }
      private set { forestsCreated = value; }
    }
    
    // METHODS

    // Define a public static method name PrintTreeFacts() that writes the value of TreeFacts to the console.
    public static void PrintTreeFacts()
    {
      Console.WriteLine(TreeFacts);
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
