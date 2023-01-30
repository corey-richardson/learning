# Introduction to Lists

At this point, we assume that you’re familiar with arrays: they’re useful tools for managing large amounts of sequential data.

But arrays have their drawbacks:

- They have a limited length
- You have to keep track of the number of elements in the array using a separate index
- You can only edit one element at a time

Lists resolve all of these issues! <br> Like arrays, they are a sequential collection of values and they can hold references to any type. Unlike arrays, they have (effectively) unlimited length, they automatically track the number of actual elements in the list, and they have handy methods to work with multiple elements at a time.

In this lesson we’ll cover list basics and some common list methods.

---

This code creates and edits a lists of cities. How does this look different from arrays?

```cs
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
```

> Output:

```
Los Angeles
Saint Petersburg
New York City
Cairo
Johannesburg
```

---

## Ranges

- AddRange() — takes an array or list as an argument. Adds the values to the end of the list. Returns nothing.
- InsertRange() — takes an int and array or list as an argument. Adds the values at the int index. Returns nothing.
- RemoveRange() — takes two int values. The first int is the index at which to begin removing and the second int is the number of elements to remove. Returns nothing.
- GetRange() — takes two int values. The first int is the index of the first desired element and the second int is the number of elements in the desired range. Returns a list of the same type.