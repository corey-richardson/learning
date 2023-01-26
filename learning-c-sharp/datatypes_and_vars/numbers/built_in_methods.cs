// Math.Abs()—will find the absolute value of a number. Example: Math.Abs(-5) returns 5.
// Math.Sqrt()—will find the square root of a number. Example: Math.Sqrt(16) returns 4.
// Math.Floor()—will round the given double or decimal down to the nearest whole number. Example: Math.Floor(8.65) returns 8.
// Math.Min()—returns the smaller of two numbers. Example: Math.Min(39, 12) returns 12.

using System;

namespace LowestNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            // Starting variables 
            int numberOne = 12932;
            int numberTwo = -2828472;

            // Use built-in methods and save to variable 
            double numberOneSqrt = Math.Floor( Math.Sqrt(numberOne) );
            double numberTwoSqrt = Math.Floor( Math.Sqrt( Math.Abs(numberTwo)) );

            // Print the lowest number
            Console.WriteLine(Math.Min(numberOneSqrt, numberTwoSqrt));
            /* Did NaN get printed to the console? NaN stands for “Not a Number” in C#.
            The built-in method Math.Sqrt() can only take a positive number as a value, 
            but the value of numberTwo is negative. But we can fix it. The method 
            Math.Abs() will find the absolute value of a number.
            */
        }
    }
}
