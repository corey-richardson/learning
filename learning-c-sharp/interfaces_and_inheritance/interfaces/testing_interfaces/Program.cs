/*
Now we have a Sedan class and Truck class that implement the IAutomobile 
interface. Though they have some different behaviors, they both have the 
properties and method defined in the interface:

double Speed
string LicensePlate
int Wheels
void Honk()
At this point we can be confident that we won’t cause any errors if we 
try to access these members in either the Sedan or Truck class.
*/

/*
1.
Create two sedans and a truck:
- a sedan with speed 60
- a sedan with speed 70
- a truck with speed 45 and weight 500

2.
Write three Console.WriteLine() statements that print the automobiles’ 
Speed, Wheels, and LicensePlate.

3.
Call SpeedUp() on all three automobiles.

4.
Using Console.WriteLine(), print out the three automobile’s new speeds.
*/

using System;

namespace LearnInterfaces
{
  class Program
  {
    static void Main(string[] args)
    {
      Sedan s1 = new Sedan(60);
      Sedan s2 = new Sedan(70);
      Truck t1 = new Truck(45, 500);

      Console.WriteLine($"s1: {s1.Speed}, {s1.Wheels}, {s1.LicensePlate}");
      Console.WriteLine($"s2: {s2.Speed}, {s2.Wheels}, {s2.LicensePlate}");
      Console.WriteLine($"t1: {t1.Speed}, {t1.Wheels}, {t1.LicensePlate}");

      s1.SpeedUp();
      s2.SpeedUp();
      t1.SpeedUp();

      Console.WriteLine($"s1: {s1.Speed}, {s1.Wheels}, {s1.LicensePlate}");
      Console.WriteLine($"s2: {s2.Speed}, {s2.Wheels}, {s2.LicensePlate}");
      Console.WriteLine($"t1: {t1.Speed}, {t1.Wheels}, {t1.LicensePlate}");
    }
  }
}