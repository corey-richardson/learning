using System;

namespace LearnInheritance
{
  class Sedan : Vehicle, IAutomobile // 3
  // Make sure that Vehicle is listed before IAutomobile. 
  // The inherited class comes before any interfaces.
  { 
    // 4
    public Sedan(double speed)
    {
      Speed = speed;
      LicensePlate = Tools.GenerateLicensePlate();
      Wheels = 4;
    }
  }
}