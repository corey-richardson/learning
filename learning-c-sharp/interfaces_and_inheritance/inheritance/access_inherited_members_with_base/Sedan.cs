using System;

namespace LearnInheritance
{
  class Sedan : Vehicle, IAutomobile
  {
    /*
    Delete the lines in the constructor that set Speed and LicensePlate
    Call the superclass constructor using : base(speed).
    */
    public Sedan(double speed) : base(speed)
    {
      Wheels = 4;
    }
    
  }
}