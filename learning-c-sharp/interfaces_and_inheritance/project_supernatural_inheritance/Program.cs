using System;

namespace MagicalInheritance
{
  class Program
  {
    static void Main(string[] args)
    {
       Pupil ppl = new Pupil("Mezil-kree");
       Storm mkStorm = ppl.CastWindStorm();
       Console.WriteLine( mkStorm.Announce() );

       Mage mg = new Mage("Gul'dan");
       Storm gdStorm = mg.CastRainStorm();
       Console.WriteLine( gdStorm.Announce() );

       Archmage na = new Archmage("Nielas Aran");
       Storm naStorm = na.CastLightningStorm();
       Console.WriteLine( naStorm.Announce() );


    }
  }
}