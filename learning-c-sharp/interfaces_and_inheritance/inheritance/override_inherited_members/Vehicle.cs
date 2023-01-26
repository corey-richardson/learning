using System;

namespace LearnInheritance
{
  class Vehicle
  {
    /* 1.
    Our new Bicycle class will access the Wheels and Speed properties in Vehicle, so make both setters protected again in Vehicle.cs. */
    public string LicensePlate
    { get; protected set; }

    public double Speed
    { get; protected set; }

    public int Wheels
    { get; protected set; }

    public Vehicle(double speed)
    {
      Speed = speed;
      LicensePlate = Tools.GenerateLicensePlate();
    }
    // 6. In Vehicle.cs, label SpeedUp() with virtual.
    public virtual void SpeedUp()
    {
      Speed += 5;
    }

    // 8. In Vehicle.cs, label SlowDown() with virtual.
    public virtual void SlowDown()
    {
      Speed -= 5;
    }
    
    public void Honk()
    {
      Console.WriteLine("HONK!");
    }

  }
}