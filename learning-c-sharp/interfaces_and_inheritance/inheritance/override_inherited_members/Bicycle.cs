using System;

namespace LearnInheritance
{
  // 2. In Bicycle.cs, create an empty Bicycle class that inherits Vehicle.
  class Bicycle : Vehicle
  {
    /* 3.
    Define a constructor that:
    - has one double parameter for setting the Speed property
    - calls base() with that parameter
    - in its body, sets Wheels to 2
    */
    // CONSTRUCTOR
    public Bicycle(double speed) : base(speed)
    {
      Speed = speed;
      Wheels = 2;
    }
    // METHOD
    /* 4.
    Define a public void SpeedUp() method that limits the Speed to 15. In other words, in the method body:
    - Add 5 to Speed
    - If Speed is greater than 15, set it to 15 */
    // 5. In Bicycle.cs, label SpeedUp() with override.
    public override void SpeedUp()
    {
      Speed += 5;
      if (Speed > 15)
      { Speed = 15; }
    }
    /* 7.
    Repeat the process with SlowDown() in Bicycle.cs (let’s assume that only sedans and trucks can go in reverse). It should override the inherited version and limit the Speed to 0. In other words, the method:
    - Subtracts 5 from Speed
    - Sets it to 0 if Speed is less than 0
    - Is labeled override
    */
    public override void SlowDown()
    {
      Speed -= 5;
      if (Speed < 0)
      { Speed = 0; }
    }
  }
}