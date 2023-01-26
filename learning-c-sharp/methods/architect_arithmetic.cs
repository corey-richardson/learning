using System;

namespace ArchitectArithmetic
{
  class Program
  {
    public static void Main(string[] args)
    {
      // 4
      double area = AreaRectangle(4,5) +
      AreaCircle(4) +
      AreaTriangle(10, 9);
      Console.WriteLine(area);

      // Floor plan
      double floorplanArea =
      AreaRectangle(1500,2500) +
      AreaCircle(375)/2 +
      AreaTriangle(500,750);
      Console.WriteLine(floorplanArea);

      double price = floorplanArea + 180;
      Console.WriteLine($"Plan costs {Math.Round(price,2)} pesos");
    }

    static double AreaRectangle(double length, double width)
    {
      return length * width;
    }

    static double AreaCircle(double radius)
    {
      return Math.PI * Math.Pow(radius,2);
    }

    static double AreaTriangle(double bottom, double height)
    {
      return (bottom * height) / 2;
    }
  }
}

/*
$ dotnet run
115.26548245743669
4158393.233455532
Plan costs 4158573.23 pesos
*/