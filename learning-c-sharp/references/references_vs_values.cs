using System;

namespace LearnReferences
{
  class Program
  {
    static void Main(string[] args)
    {
      // Create a Book variable bookLocation that refers to a new Book object.
      // The variable is a reference to the object’s location in memory.
      Book bookLocation = new Book();

      // Create another Book variable named sameBookLocation and set it equal
      // to bookLocation.
      // Both variables refer to the same location in memory.
      Book sameBookLocation = bookLocation;

      // Create a bool variable falseValue that refers to the boolean value 
      // false.
      // The variable holds the actual value.
      bool falseValue = false;

      // Create another bool variable anotherFalseValue and set it equal to
      // falseValue.
      // The false value was copied to a new location in memory for
      // anotherFalseValue to use.
      bool anotherFalseValue = falseValue;
      
    }
  }
}
