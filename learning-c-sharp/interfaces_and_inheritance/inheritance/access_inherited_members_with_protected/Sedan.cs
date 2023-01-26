using System;

namespace LearnInheritance
{
  class Sedan : Vehicle, IAutomobile
  {
    public Sedan(double speed)
    {
      Speed = speed;
      LicensePlate = Tools.GenerateLicensePlate();
      Wheels = 4;
    }
    
  }
}