///////////////////////////////////////////////////////////////////////////////
// 1. Fix error CS0515.
/*
error CS0515: 'Forest.Forest()': static constructor cannot have an 
access modifier
*/

/*
    public static Forest()
    {
      treeFacts = "Forests provide a diversity of ecosystem services including:\r\n  aiding in regulating climate.\r\n  purifying water.\r\n  mitigating natural hazards such as floods.\n";
      ForestsCreated = 0;
    }
*/
// remove 'public' 
/*
    static Forest()
    {
      treeFacts = "Forests provide a diversity of ecosystem services including:\r\n  aiding in regulating climate.\r\n  purifying water.\r\n  mitigating natural hazards such as floods.\n";
      ForestsCreated = 0;
    }
*/
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
// 2. Fix error CS0120.
/*
error CS0120: An object reference is required to access non-static field, 
method, or property 'Forest.Grow()'
*/
/*
Forest f = new Forest("Congo", "Tropical");
Forest.Grow();
*/
// Forest --> f
/*
Forest f = new Forest("Congo", "Tropical");
f.Grow();
*/
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
// 3. Fix error CS0176.
/*
error CS0176: Member 'Forest.TreeFacts' cannot be accessed with an instance 
reference; qualify it with a type name instead
*/

/*
Console.WriteLine(f.TreeFacts);
*/
// f --> Forest
/*
Console.WriteLine(Forest.TreeFacts);
*/
///////////////////////////////////////////////////////////////////////////////

using System;

namespace StaticMembers
{
  class Forest
  {
    // FIELDS
    
    public int age;
    private string biome;
    private static int forestsCreated;
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
    
    static Forest()
    {
      treeFacts = "Forests provide a diversity of ecosystem services including:\r\n  aiding in regulating climate.\r\n  purifying water.\r\n  mitigating natural hazards such as floods.\n";
      ForestsCreated = 0;
    }
    
    // PROPERTIES
    
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
    
    public static string TreeFacts
    {
      get { return treeFacts; }
    }
    
    // METHODS
     
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
    
    public static void PrintTreeFacts()
    {
      Console.WriteLine(TreeFacts);
    }
    
  }

}