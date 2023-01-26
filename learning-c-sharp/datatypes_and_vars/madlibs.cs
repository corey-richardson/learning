/*
Mad Libs require: A short story with blank spaces (asking for different types 
of words). Words from the player to fill in those blanks.

For this project, we have provided the story, but it will be up to you to 
complete the following: Prompt the user for inputs. Print the story with the 
inputs in the right places.

It’s important to note that for this project, you should test your app 
periodically — when you hit save, your app will not run! To run your app, 
enter 'dotnet run' into the terminal.
*/

using System;

namespace MadLibs
{
  class Program
  {
    static void Main(string[] args)
    {
      /*
      This program madlibs
      Author: me
      */


      // Let the user know that the program is starting:
      Console.WriteLine("User, the program is starting");

      // Give the Mad Lib a title:
      string title = "A TITLE";

      Console.WriteLine(title);
      // Define user input and variables:
      Console.WriteLine("Name: ");
      string name_1 = Console.ReadLine();
      Console.WriteLine("Adjective: ");
      string adj_1 = Console.ReadLine();
      Console.WriteLine("Adjective: ");
      string adj_2 = Console.ReadLine();
      Console.WriteLine("Animal: ");
      string animal = Console.ReadLine();
      Console.WriteLine("Food: ");
      string food = Console.ReadLine();
      Console.WriteLine("Verb: ");
      string verb = Console.ReadLine();
      Console.WriteLine("Noun: ");
      string noun_1 = Console.ReadLine();
      Console.WriteLine("Fruit: ");
      string fruit = Console.ReadLine();
      Console.WriteLine("Adjective: ");
      string adj_3 = Console.ReadLine();
      Console.WriteLine("Name: ");
      string name_2 = Console.ReadLine();
      Console.WriteLine("Superhero: ");
      string superhero = Console.ReadLine();
      Console.WriteLine("Name: ");
      string name_3 = Console.ReadLine();
      Console.WriteLine("Country: ");
      string country = Console.ReadLine();
      Console.WriteLine("Name: ");
      string name_4 = Console.ReadLine();
      Console.WriteLine("Dessert: ");
      string dessert = Console.ReadLine();
      Console.WriteLine("Name: ");
      string name_5 = Console.ReadLine();
      Console.WriteLine("Year: ");
      string year = Console.ReadLine();
      Console.WriteLine("Noun: ");
      string noun_2 = Console.ReadLine();

      // The template for the story:
      string story = $"This morning {name_1} woke up feeling {adj_1}. 'It is going to be a {adj_2} day!' Outside, a bunch of {animal}s were protesting to keep {food} in stores. They began to {verb} to the rhythm of the {noun_1}, which made all the {fruit}s very {adj_3}. Concerned, {name_2} texted {superhero}, who flew {name_3} to {country} and dropped {name_4} in a puddle of frozen {dessert}. {name_5} woke up in the year {year}, in a world where {noun_2}s ruled the world.";


      // Print the story:
      Console.WriteLine(story);
    }
  }
}


/*
$ dotnet run
User, the program is starting
A TITLE
Name: 
Corey
Adjective: 
red
Adjective: 
cold
Animal: 
duck
Food: 
duck dumplings
Verb: 
boogy
Noun: 
computer
Fruit: 
pomegranate
Adjective: 
fast
Name: 
Dave
Superhero: 
Captain Dave
Name: 
John
Country: 
Azerbajin
Name: 
Neil
Dessert: 
trifle
Name: 
Andy
Year: 
2004
Noun: 
hazelnut

Corey woke up feeling red. 'It is going to be a cold day!' Outside, a bunch of 
ducks were protesting to keep duck dumplings in stores. They began to boogy to 
the rhythm of the computer, which made all the pomegranates very fast. 
Concerned, Dave texted Captain Dave, who flew John to Azerbajin and dropped 
Neil in a puddle of frozen trifle. Andy woke up in the year 2004, in a world 
where hazelnuts ruled the world.
$ 