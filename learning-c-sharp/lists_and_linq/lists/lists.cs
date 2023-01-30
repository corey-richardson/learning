using System;
using System.Collections.Generic;

namespace LearnLists
{
  class Program
  {
    static void Main()
    {
      List<string> citiesList = new List<string> { "Delhi", "Los Angeles", "Saint Petersburg" };      
      citiesList.Add("New York City");      
      citiesList.Remove("Delhi");
      citiesList.AddRange(new string[] {"Cairo", "Johannesburg"});
      
      bool hasNewDelhi = citiesList.Contains("New Delhi");
      
      foreach (string city in citiesList)
      {
        Console.WriteLine(city);
      }
    }
  }
}