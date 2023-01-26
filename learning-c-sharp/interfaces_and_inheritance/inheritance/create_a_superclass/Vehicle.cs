using System;

namespace LearnInheritance
{
  class Vehicle // 1
  {
    // 2
    // PROPERTIES
    public string LicensePlate
    { get; }
    public double Speed
    { get; private set; }
    public int Wheels
    { get; }
    
    // METHODS
    public void Honk()
    { Console.WriteLine("HONK!"); }
    public void SpeedUp()
    { Speed += 5; }
    public void SlowDown()
    { Speed -= 5; }

  }
}

