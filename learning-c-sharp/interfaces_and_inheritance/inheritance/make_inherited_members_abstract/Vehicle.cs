using System;

namespace LearnInheritance
{
  // 1. Vehicle will also need to be labeled abstract
  abstract class Vehicle
  {
    public string LicensePlate
    { get; private set; }

    public double Speed
    { get; protected set; }

    public int Wheels
    { get; protected set; }

    public Vehicle(double speed)
    {
      Speed = speed;
      LicensePlate = Tools.GenerateLicensePlate();
    }

    public virtual void SpeedUp()
    {
      Speed += 5;
    }

    public virtual void SlowDown()
    {
      Speed -= 5;
    }
    
    public void Honk()
    {
      Console.WriteLine("HONK!");
    }

    // ABSTRACT METHOD
    // 1. Describe() should be public and return a string
    public abstract string Describe();

    /* 2.
    Implement Describe() methods in Bicycle, Sedan, and Truck. Each method should:
    - mention the type, e.g. the bicycle version of the method returns a string containing "bicycle"
    - mention the license plate, speed, and wheels
    - be labeled with override
    */

  }
}