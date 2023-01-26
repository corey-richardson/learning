using System;

namespace DatingProfile
{
  class Program
  {
    static void Main(string[] args)
    {
      Profile sam = new Profile
      ("Sam Drakkila",30,"New York","USA","he/him");

      
      sam.SetHobbies(new string[] {
        "listening to audiobooks and podcasts", 
        "playing rec sports like bowling and kickball", 
        "writing a speculative fiction novel", 
        "reading advice columns"
      });

      sam.ViewProfile();
    }
  }
}
