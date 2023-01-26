// returns the remainder

using System;

namespace ClassTeams
{
  class Program
  {
    static void Main(string[] args)
    {
      // Number of students
      int students = 18;
      // Number of students in a group
      int groupSize = 3;
      // Does groupSize go evenly into students?
      Console.WriteLine(students % groupSize);

    }
  }
}
