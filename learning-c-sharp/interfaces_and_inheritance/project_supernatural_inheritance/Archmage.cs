// Archmage.cs
using System;

namespace MagicalInheritance
{
  class Archmage : Mage
  {
    // CONSTRUCTOR
    public Archmage(string title) : base(title)
    {
      Title = title;
    }

    // METHODS
    // Override CastRainStorm()
    public override Storm CastRainStorm()
    {
      Storm strm = new Storm("rain", true, Title);
      return strm; 
    }
    public Storm CastLightningStorm()
    {
      Storm strm = new Storm("lightning", true, Title);
      return strm;
    }
  }
 
}
