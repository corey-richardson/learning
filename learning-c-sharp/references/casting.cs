/*
In Program.cs, Dissertation and Diary type references are being EXPLICITLY 
upcast to the Book type. We know that those explicit casts aren’t necessary.
Delete the explicit casts from both lines.

Book bdiss = (Book)diss;
Book bdy = (Book)dy;
*/

using System;

namespace LearnReferences
{
  class Program
  {
    static void Main(string[] args)
    {
			Dissertation diss = new Dissertation();
      Diary dy = new Diary();
      
      Book bdiss = diss;
      Book bdy = dy;
    }
  }
}
