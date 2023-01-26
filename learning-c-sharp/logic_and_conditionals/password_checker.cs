using System;

namespace PasswordChecker
{
  class Program
  {
    public static void Main(string[] args)
    {
      int minLength = 5;
      string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      string lowercase = "abcdefghijklmnopqrstuv";
      string digits = "0123456789";
      string specialChars = "!£$%^&*@~#,./";

      Console.WriteLine("Enter Password: ");
      string password = Console.ReadLine();

      int score = 0;

      // check length
      if (password.Length >= minLength)
      {
        score++;
      }

      // We’ve provided a custom tool that checks for certain characters in a string, called Tools.Contains().
      if (Tools.Contains(password,uppercase))
      {
        score++;
      }
      if (Tools.Contains(password,lowercase))
      {
        score++;
      }
      if (Tools.Contains(password,digits))
      {
        score++;
      }
      if (Tools.Contains(password,specialChars))
      {
        score++;
      }

      Console.WriteLine(score);

      switch (score){
        case 1:
        Console.WriteLine("Weak");
        break;
        case 2:
        Console.WriteLine("Medium");
        break;
        case 3:
        Console.WriteLine("Strong");
        break;
        case 4:
        case 5:
        Console.WriteLine("Extremely strong");
        break;
        default:
        Console.WriteLine("Doesn't meet standards.");
        break;
      }
    }
  }
}
