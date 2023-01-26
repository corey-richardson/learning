/*
1.
Add a public double Weight property with just a getter.

2.
Add a constructor to the Truck class with two parameters: 
double speed and double weight. It should:

- Set the Speed property using speed
- Set the Weight property using weight
- Set a random LicensePlate value using Tools.GenerateLicensePlate()
- Set Wheels to 8 if Weight is less than 400 and set Wheels to 12 otherwise

3.
Add a void SpeedUp() method that increases the Speed property by 5.

4.
Did you get an error? There is no setter for the Speed property. Add a 
private setter to that property.

5.
Add a void SlowDown() method that decreases the Speed by 5.
*/

using System;

namespace LearnInterfaces
{
  class Truck : IAutomobile
  {
  	public string LicensePlate
    { get; }
    public double Speed
    { get; set; } // 4.
    public int Wheels
    { get; }
    public void Honk()
    {
      Console.WriteLine("HONK!");
    }

    // 1.
    public double Weight
    { get; }

    // 2.
    public Truck(double speed, double weight)
    {
      Speed = speed;
      Weight = weight;
      LicensePlate = Tools.GenerateLicensePlate();

      if (Weight < 400)
      {
        Wheels = 8;
      } else {
        Wheels = 12;
      }
    }

    // 3.
    public void SpeedUp()
    {
      Speed += 5;
    }
    // 5.
    public void SlowDown()
    {
      Speed -= 5;
    }

  }
}