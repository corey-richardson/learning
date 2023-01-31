using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace ProgrammingLanguages
{
  class Program
  {
    static void Main()
    {
      List<Language> languages = File.ReadAllLines("./languages.tsv")
        .Skip(1)
        .Select(line => Language.FromTsv(line))
        .ToList();
    
      // Let’s start by printing all of the languages: print each item in 
      // languages by calling its Prettify() method.
      /*
      foreach (Language lang in languages)
      { Console.WriteLine( lang.Prettify() ); }
      */

      // Write a query that returns a string for each language. It should
      // include the year, name, and chief developer of each language.
      var myPretty = languages
      .Select(l => $"{l.Year} | {l.Name} | {l.ChiefDeveloper}");
      /*
      foreach (string mp in myPretty)
      { Console.WriteLine(mp); }
      */

      // Find the language(s) with the name "C#". Use the Prettify() method
      // to print the results to the console.
      Console.WriteLine("\nC#");
      var csharp = languages
      .Where(l=> l.Name == "C#")
      .Select(c=> c.Prettify());
      foreach(string cs in csharp)
      {Console.WriteLine(cs);}

      // Find all of the languages which have "Microsoft" included in their
      // ChiefDeveloper property.
      Console.WriteLine("\nMicrosoft");
      var msoft = languages
      .Where(l=> l.ChiefDeveloper == "Microsoft")
      .Select(c=> c.Prettify());
      foreach(string ms in msoft)
      {Console.WriteLine(ms);}

      // Find all of the languages that descend from Lisp.
      Console.WriteLine("\nLisp");
      var lisp = languages
      .Where(l=> l.Predecessors.Contains("Lisp"))
      .Select(c=> c.Prettify());
      foreach(string lsp in lisp)
      {Console.WriteLine(lsp);}

      // Find all of the language names that contain the word "Script" (capital S).
      // Make sure the query only selects the name of each language.
      Console.WriteLine("\nScript");
      var nameContainsScript = languages
      .Where(l=> l.Name.Contains("Script"))
      .Select(c=> c.Name);
      PrintAll(nameContainsScript);

      // How many languages are included in the languages list?
      Console.WriteLine("\nCount");
      Console.WriteLine(languages.Count());

      // How many languages were launched between 1995 and 2005?
      // Print a string for each of those near-millennium languages.
      Console.WriteLine("\n1995-2005");
      var millenials = languages
      .Where(l=> 1995 <= l.Year && l.Year <= 2005)
      .Select(p=> $"{p.Name} was invented in {p.Year}");
      Console.WriteLine(millenials.Count());
      PrintAll(millenials);

      Console.WriteLine("\nCheckpoint 10:");
      PrettyPrintAll(languages);
      
    }
      // You might have used foreach loops to print every Language in this project.
      // Write a method PrettyPrintAll() that handles that for us.
      public static void PrettyPrintAll(IEnumerable<Language> langs)
        {
          foreach (var l in langs)
          {
            Console.WriteLine(l.Prettify());
          }
        }
      
      // You might have also used foreach loops to print every query result in
      // this project. Write a method PrintAll() that handles that for us
      public static void PrintAll(IEnumerable<Object> query)
      {
        foreach(string query_item in query)
        {Console.WriteLine(query_item); }
      }

  }
}
