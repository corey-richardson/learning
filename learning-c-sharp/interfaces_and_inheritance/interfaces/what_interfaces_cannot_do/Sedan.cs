/*
1.
Add a constructor to the Sedan class with one parameter, speed, of type 
double. It should

- set the Speed property to speed
- set a random LicensePlate value
- set Wheels to 4

To make a random license plate, a utility class is provided for you. 
Use it in the constructor like so: Tools.GenerateLicensePlate().

2.
Add a void SpeedUp() method that increases the Speed property by 5.

3.
Did you get an error? There is no setter for the Speed property. 
Add a private setter such as private set to the Speed property.

4.
Add a void SlowDown() method that decreases the Speed by 5.
*/

using System;

namespace LearnInterfaces
{
  class Sedan : IAutomobile
  {
    // 1. CONSTRUCTOR
    public Sedan(double speed)
    {
      Speed = speed;
      // LicensePlate = "RES 1536"; // toy story yay
      LicensePlate = Tools.GenerateLicensePlate();
      Wheels = 4;
    }

    // METHODS
    // 2.
    public void SpeedUp()
    {
      Speed += 5;
    }

    // 4.
    public void SlowDown()
    {
      Speed -= 5;
    }

    // PROPERTIES
  	public string LicensePlate
    { get; }
    
    // 3.
    public double Speed
    { get; set; }

    public int Wheels
    { get; }
    
    public void Honk()
    {
      Console.WriteLine("HONK!");
    }
  }
}