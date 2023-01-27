// Pupil.cs
using System;

namespace MagicalInheritance
{
  class Pupil
  {
    // PROPERTIES
    public string Title
    { get; protected set; }
    
    // CONSTRUCTOR
    public Pupil(string title)
    {
      Title = title;
    }

    // METHODS
    public Storm CastWindStorm()
    {
      Storm strm = new Storm("wind", false, Title);
      return strm;
    }
  }
  
}
