using System;

namespace TrueOrFalse
{
  class Program
  {
		static void Main(string[] args)
    {
      // Do not edit these lines
      Console.WriteLine("Welcome to 'True or False?'\nPress Enter to begin:");
      string entry = Console.ReadLine();
      Tools.SetUpInputStream(entry);

      // Type your code below
      string[] questions = {
      "Yes?",
      "Yes?",
      "No?",
      "Yes?",
      "No?"
      };

      bool[] answers = {
      true,
      true,
      false,
      true,
      false
      };

      bool[] responses = new bool[questions.Length];

      if (questions.Length != answers.Length)
      {
        Console.WriteLine($"WARNING: questions array and answers array of unequal lengths. {questions.Length} / {answers.Length}");
      }
      
      int askingIndex = 0;
      foreach (string question in questions)
      {
        string input;
        bool isBool = false;
        bool inputBool;

        while (!isBool)
        { 
          Console.WriteLine(question);
          Console.WriteLine("True or false?");
          input = Console.ReadLine();

          if (!(input == "true" || input == "false"))
          {
            Console.WriteLine("Please respond with 'true' or 'false'.");
            continue;
          }
          isBool = Boolean.TryParse(input, out inputBool);
        }
        responses[askingIndex] = inputBool;
        askingIndex++;
      }
      foreach (bool response in responses)
      {
        Console.WriteLine(response);
      }
    }
  }
}
