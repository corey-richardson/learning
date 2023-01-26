// To make a static field and property, just add static after the access modifier (public or private).

/*
class Forest
{
  private static string definition;
  public static string Definition
  { 
    get { return definition; }
    set { definition = value; }
  }
}
*/

// static means “associated with the class, not an instance”.
// Thus any static member is accessed from the class, not an instance:

/*
static void Main(string[] args)
{
  Console.WriteLine(Forest.Definition);
}
*/

using System;

namespace StaticMembers
{
  class Forest
  {
    // FIELDS
    
    public int age;
    private string biome;

    // In the previous exercise we mentioned storing the count of all Forest objects.
    // We’ll use a static field and property to store that.
    // Define a private static field named forestsCreated.
    private static int forestsCreated;
    
    // CONSTRUCTORS
    
    public Forest(string name, string biome)
    {
      this.Name = name;
      this.Biome = biome;
      Age = 0;
      // In the first constructor, increment ForestsCreated.
      // This will add 1 to the property every time an object is constructed.
      Forest.ForestsCreated ++;
    }
    
    public Forest(string name) : this(name, "Unknown")
    { }
    
    // PROPERTIES

    // Define a public static property named ForestsCreated. 
    // Give it a public getter and private setter.
    public static int ForestsCreated
    {
      get { return forestsCreated; }
      private set { forestsCreated = value; }
    }
    
    public string Name
    { get; private set; }
    
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
    
  }

}
