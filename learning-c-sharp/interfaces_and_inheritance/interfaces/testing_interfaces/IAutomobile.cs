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