using System;

// 1. Add a reference to the System.Collections.Generic namespace.
using System.Collections.Generic;

// 2.
// Declare three empty lists:
// one should hold bool types
// one should hold Random types
// one should hold IServiceProvider types

namespace LearnLists
{
  class Program
  {
    static void Main()
    {
      List<bool> bools = new List<bool>();
      List<Random> rands = new List<Random>();
      List<IServiceProvider> isps = new List<IServiceProvider>();
    }
  }
}
