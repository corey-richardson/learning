using System;

namespace LearnInheritance
{
  class Truck : Vehicle, IAutomobile
  { 
    public double Weight
    { get; }
    /*
    Delete the lines in the constructor that set Speed and LicensePlate
    Call the superclass constructor using : base(speed)
    */
    public Truck(double speed, double weight) : base(speed)
    {
      Weight = weight;

      if (weight < 400)
      {
        Wheels = 8;
      }
      else
      {
        Wheels = 12;
      }
    }

  }
}