using System;

namespace LearnReferences
{
  class Program
  {
    static void Main(string[] args)
    {
      Dissertation diss1 = new Dissertation(32, "Anna Knowles-Smith", "Refugees and Theatre");
			Dissertation diss2 = new Dissertation(19, "Lajos Kossuth", "Shiny Happy People");
			Diary dy1 = new Diary(48, "Anne Frank", "The Diary of a Young Girl");
			Diary dy2 = new Diary(23, "Lili Elbe", "Man into Woman");
			
      // 1. Create a variable books of type Book[] that contains:
      // diss1, diss2, dy1, and dy2.
      Book[] books = new Book[] {diss1, diss2, dy1, dy2};
      // 2. Make an empty foreach loop that loops through each
      // element in the array.
      foreach (Book book in books){
        // 3. In the body of the loop, print out the Title of each element.
        Console.WriteLine( book.Title );

      }
      
    }
  }
}
