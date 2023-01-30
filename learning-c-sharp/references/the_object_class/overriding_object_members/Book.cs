/*
In Book.cs, define an override ToString() method for the Book class.
It should return a string containing the Author and Title information.
*/
namespace TheObjectClass
{
  class Book
  {
    public string Author
    { get; private set; }
    
    public string Title
    { get; private set; }

    public Book(string author = "Unknown", string title = "Untitled")
    {
      Author = author;
      Title = title;
    }

    public virtual string Stringify()
    {
      return "This is a Book object!";
    }

    public override string ToString(){
      return $"{Title} by {Author}";
    }
  }
}