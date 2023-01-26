/*
For this lesson we will be designing a new set of transportation machines that satisfy the requirements of BOTH car designers and the highway patrol. First the highway patrol tells us: “Every automobile on the road must have these properties and methods accessible to us:”

speed
license plate number
number of wheels
ability to honk
*/

/*
Add these three properties and one method to the interface:

a string called LicensePlate
a double called Speed
an int called Wheels
a void method called Honk()

The properties only need a getter. Use the get shorthand demonstrated in the narrative for Id.
*/
using System;

namespace LearnInterfaces
{
  interface IAutomobile
  {
    string LicensePlate { get; }
    double Speed { get; }
    int Wheels { get; }
    void Honk();
  }
}