using System;

namespace LearnInheritance
{
  class Vehicle
  {
    /*
    Remember that a class has a default parameterless constructor if no constructor is explicitly defined. This is the case with Vehicle.

When we define a constructor, like Vehicle(double speed), that parameterless constructor is no longer available.
*/
    public Vehicle(double speed)
    {
      Speed = speed;
      LicensePlate = Tools.GenerateLicensePlate();
    }

    /*
    4.
Since the LicensePlate and Speed properties defined in Vehicle are no longer accessed in Sedan or Truck, they no longer need to be protected. Switch those two setters to private.
    */
    public string LicensePlate
    { get; private set; }

    public double Speed
    { get; private set; }

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