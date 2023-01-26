using System;

namespace DatingProfile
{ 
  class Profile
  {
    // FIELDS
    private string name;
    private int age;
    private string city;
    private string country;
    private string pronouns;
    private string[] hobbies;

    // CONSTRUCTOR
    public Profile
    (string name, int age, string city, string country,
    string pronouns = "they/them")
    {
      this.name = name;
      this.age = age;
      this.city = city;
      this.country = country;
      this.pronouns = pronouns;
    }

    // METHODS
    public void ViewProfile()
    {
      string profile_string = $"Name: {name} \nAge: {age} \nLocation: {city}, {country} \nPronouns: {pronouns}";

      Console.WriteLine(profile_string);
      Console.WriteLine("Hobbies:");
      foreach (string hobby in hobbies)
      {
        Console.WriteLine(hobby);
      }

    }

    public void SetHobbies(string[] hobbies)
    {
      this.hobbies = hobbies;
    }
  }
}


/*
$ dotnet run
Name: Sam Drakkila 
Age: 30 
Location: New York, USA 
Pronouns: he/him
Hobbies:
listening to audiobooks and podcasts
playing rec sports like bowling and kickball
*/