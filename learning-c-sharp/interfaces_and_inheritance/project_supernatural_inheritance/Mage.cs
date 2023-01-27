// Mage.cs
using System;

namespace MagicalInheritance
{
  class Mage : Pupil
  {
    // CONSTRUCTOR
    // Call base constructor
    public Mage(string title) : base(title)
    {
      Title = title;
    }

    // METHODS
    public virtual Storm CastRainStorm()
    {
      Storm strm = new Storm("rain", false, Title);
      return strm;
    }
    
  }
}
