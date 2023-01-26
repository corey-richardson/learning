using System;

namespace MethodOverloading
{
  class Program
  {
    static void Main(string[] args)
    {
      NamePets("Mister","Perry the Platypus");
      NamePets("Mister","Perry the Platypus","Alby");
      NamePets();
    }
    static void NamePets(string name_1, string name_2)
    {
      Console.WriteLine($"Your pets {name_1} and {name_2} will be joining your voyage across space!");
    }
    static void NamePets(string name_1, string name_2, string name_3)
    { // overloaded to accept 3 parameters
      Console.WriteLine($"Your pets {name_1}, {name_2} and {name_3} will be joining your voyage across space!");
    }
    static void NamePets()
    { // overloaded to accept no parameters
      Console.WriteLine("Aw, you have no spacefaring pets :(");
    }
  }
}
