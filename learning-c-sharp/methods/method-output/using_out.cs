using System;

namespace UsingOut
{
  class Program
  {
    static void Main(string[] args)
    {
      msgLower = Whisper("HELLO THERE", out bool flag);
    }   

    static string Whisper(string msg, out bool flag)
    {
      flag = true;
      return msg.ToLower();
    } 
    
	}
}
