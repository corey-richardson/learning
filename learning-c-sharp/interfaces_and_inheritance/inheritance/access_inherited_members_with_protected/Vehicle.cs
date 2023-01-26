/*
In Vehicle, add a protected setter to each of these properties:
- LicensePlate
- Speed
- Wheels
*/

using System;

namespace LearnInheritance
{
  class Vehicle
  {
    public string LicensePlate
    { get; protected set; }

    public double Speed
    { get; protected set; }

    public int Wheels
    { get; protected set; }

    public void SpeedUp()
    {
      Speed += 5;
    }

    public void SlowDown()
    {
      Speed -= 5;
    }
    
    public void Honk()
    {
      Console.WriteLine("HONK!");
    }

  }
}

/*
Output:

Sedan.cs(9,7): error CS0272: The property or indexer 'Vehicle.Speed' cannot 
be used in this context because the set accessor is inaccessible 
[/home/ccuser/workspace/csharp-inheritance-protected/LearnInheritance.csproj]

Sedan.cs(10,7): error CS0200: Property or indexer 'Vehicle.LicensePlate' 
cannot be assigned to -- it is read only 
[/home/ccuser/workspace/csharp-inheritance-protected/LearnInheritance.csproj]

Sedan.cs(11,7): error CS0200: Property or indexer 'Vehicle.Wheels' cannot 
be assigned to -- it is read only 
[/home/ccuser/workspace/csharp-inheritance-protected/LearnInheritance.csproj]

-->

Sedan with license plate W7HDI1PY and 4 wheels, driving at 60 km/h.
Sedan's faster speed: 65
Sedan with license plate ZU251CSG and 4 wheels, driving at 70 km/h.
Sedan's faster speed: 75
Truck with license plate 0LNUW9HP and 12 wheels, driving at 45 km/h.
Truck's faster speed: 50
*/