namespace LearnReferences
{
  interface IFlippable
  {
    int CurrentPage { get; set; }
    void Flip();
  }
}