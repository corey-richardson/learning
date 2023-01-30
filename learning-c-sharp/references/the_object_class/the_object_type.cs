/*
When we write this code:
```
class Book
{}
```

C# assumes we mean:
```
class Book : Object
{}
```
*/

// There are three references created in Program.cs, one of type Book, one of
// type Diary, and one of type int.
// Create a new Object reference for each one.

using System;

namespace TheObjectClass
{
  class Program
  {
    static void Main(string[] args)
    {
      Book bk = new Book();
      
      Diary dy = new Diary(38);
      
      int i = 9;

      Object r_bk = bk;
      Object r_dy = dy;
      Object r_i = i;

    }
  }
}
