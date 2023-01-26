using System;

namespace LearnInterfaces
{
  // In Sedan.cs, create an empty Sedan class that implements the IAutomobile 
  // interface. Use colon (:) notation.
 class Sedan : IAutomobile
 {
   /*
   You should see the error CS0535 telling you that the Sedan needs to 
   implement the interface! Implement the interface by adding the three 
   properties and one method defined in IAutomobile, which you can check 
   in IAutomobile.cs.
   */
   public string LicensePlate
   { get; }
   public double Speed
   { get; }
   public int Wheels
   { get; }
   public void Honk()
   { Console.WriteLine("Honk"); }

 }
}