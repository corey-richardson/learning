/*
At this point we have built fields to associate data with a class and 
properties to control the getting and setting of each field. As it is now, any 
code outside of the Forest class can “sneak past” our properties by directly 
accessing the field:

f.Age = 32; // using property
f.age = -1; // using field

The second line avoids the property’s validation by directly accessing the field. 
We can fix this by using the access modifiers public and private:

public — a public member can be accessed by any class
private — a private member can only be accessed by code in the same class

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
      f.Biome = "Desert";
      
      Console.WriteLine(f.Name);
      Console.WriteLine(f.Biome);
    }
  }
}
