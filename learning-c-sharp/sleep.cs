using System;
using System.Threading; // INCLUDE SYSTEM.THREADING

namespace Sleep
{
    class Program
    {
        static void Main()
        {
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"Hello World! {i+1}");
                Thread.Sleep(1000); // Thread.Sleep(milliseconds)
                
            }
        }
    }
}

// INCLUDE SYSTEM.THREADING
// Thread.Sleep(milliseconds)