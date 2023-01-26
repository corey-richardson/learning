Define encapsulation
- Bundling related data and methods into one logical groups.

Which of the is not a class member?
Method / Property / Object / Constructor
- Object

An instance of the Random class is constructed below. Call the instance method Next(), which returns a random integer.
- int guess = *Random*.Next()
**x**
- int guess = **instance**.Member()

What is a class?
- The definition of a cutsom type

Create an instance of the Chainsaw class, which has a parameterless constructor.
- Chainsaw cutter = new Chainsaw();

What is an object?
- An instance of a class

When Main() is run, what will be printed to the console?
```
class Program {
  public static void Main (string[] args) {
    Player p = new Player();
  }
}
 
class Player
{
  public Player(string name)
  {
    Console.WriteLine($"Player named: {name}");
  }
 
  public Player() : this("n/a")
  {}
}
```
- "Player named: n/a"

Given the Breakfast class, what is ingredients?
```
class Breakfast 
{
  string[] ingredients;
}
```
- A property **x**
- A field, *a property would have a type in its definition.*

Given the SpaceInvader class, what is Speed?
```
class SpaceInvader 
{
  public SpaceInvader()
  {
    this.Speed = 5;
  }
 
  public bool IsMothership
  { get; set; }
 
  public int Speed
  { get; set; }
}
```
- A property

Given the Unicorn class, which line in Main() will cause an error?
```
class Program {
  public static void Main (string[] args) {
    Unicorn u = new Unicorn();
    Console.WriteLine(u.HornLength);
    u.HornLength = 5;
    int len = u.HornLength;
  }
}
 
class Unicorn
{
  public int HornLength
  { get; private set; }
}
```
- int len = u.HornLength; *The get method for HornLength is public, so this line will not cause an error.*
- **u.HornLength = 5;**

Given the SpaceInvader class, what is SpaceInvader()?
```
class SpaceInvader 
{
  public SpaceInvader()
  {
    this.Speed = 5;
  }
 
  public bool IsMothership
  { get; set; }
 
  public int Speed
  { get; set; }
}
```
- A constructor method

## **8/11 | 8 correct, 3 to work on | 72%**
