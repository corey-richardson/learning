// break
// At any point within a loop block, you can end it by using the break keyword.

// continue
// The continue keyword is used to bypass portions of code. It will ignore 
// whatever comes after it in the loop and then will go back to the top and 
// start the loop again.

// return
// The return keyword is another way to exit a loop, specifically loops that 
// are used within a method. When a return is used within such a loop, it breaks
// out of the loop and returns control to the point in the program where the 
// method was called.

/*
You’ve decided to go back to the pomodoro application. This time, you don’t want 
the alarm to ring endlessly. Once it rings 3 times, it should shut off even if 
the button has not been clicked.
*/
using System;

namespace JumpStatements
{
  class Program
  {
    static void Main(string[] args)
    {
      bool buttonClick = false;
      
      int ringCounter = 0;
      do
      {
        Console.WriteLine("BLARRRRR");
        ringCounter++;
        if (ringCounter >= 3) {break;}

        
      } while(!buttonClick);
    }
  }
}
