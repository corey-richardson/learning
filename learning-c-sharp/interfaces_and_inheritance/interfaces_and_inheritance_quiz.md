1. Fill in the code so that the WorkerBee class inherits from the Bee class.

```cs
class WorkerBee : Bee
{}
```

2. What does it mean for a class member to be abstract?
- The member has a missing or incomplete implementation. It must be implemented by derived classes.
- The member cannot be accessed by derived classes.
- The member can be accessed by any class.
- **The member overrides an inherited member.**

> The member has a missing or incomplete implementation. It must be implemented by derived classes. <br>
> It is possible for an abstract member to override an inherited member. However, that is not the meaning of abstract.

3. Given that IMachine is an interface, what does the first line mean?

```cs
class Tractor : IMachine
{}
```
- There is one class named Tractor : IMachine.
- Calling Tractor() will call IMachine().
- **The Tractor class implements the IMachine interface.**
- The IMachine interface implements the Tractor class.

4. Fill in the code so that Giganotosaurus.Warn() overrides the Dinosaur.Warn() method.

```cs
class Dinosaur
{
  public ___ void Warn()
  {
    Console.WriteLine("Wow, a dino!");
  }
}
 
class Giganotosaurus : Dinosaur
{
  public ___ void Warn()
  {
    Console.WriteLine("Wow, a GIANT dino!");
  }
}
```

*abstract |
override |
virtual*

```cs
class Dinosaur
{
  public abstract void Warn()
  {
    Console.WriteLine("Wow, a dino!");
  }
}
 
class Giganotosaurus : Dinosaur
{
  public override void Warn()
  {
    Console.WriteLine("Wow, a GIANT dino!");
  }
}
```

> abstract --> virtual <br>
> virtual marks the method in the base class to be overridden. override marks the method in the derived class.

5. Fill in the code so that Calculator extends the Computer class and implements the IClickable interface.

```cs
class Computer  : Calculator, IClickable
```
-->
```cs
class Calculator  : Computer, IClickable
```
> sidenote: that question is worded AWFULLY

6. What is inheritance?
- A type of class
- **The process by which one class inherits the members of another class**
- The process of writing duplicate code in multiple classes
- A definition for a group of related functionalities that a class can implement

7. Why will this code cause an error?

```cs
interface IPersonable
{
  DateTime BirthDate { get; }
  string FullName { get; }
}
 
class Passport : IPersonable
{}
```
- IPersonable is not a legal interface name.
- **The Passport class does not correctly implement the interface.**
- The interface is missing member implementations.
- Interfaces cannot contain properties.

8. This code will throw errors. What change will fix those errors?

```cs
class Building
{
  private int x;
  private int y;
}
 
class Garage : Building
{
  public string ListValues()
  {
    return $"x: {this.x}, y: {this.y}";
  }
}
```

- Change both private fields to override.
- Change both private fields to virtual.
- Change both private fields to abstract.
- **Change both private fields to protected.**

9. Fill in the code so that WorkerBee implements the IFlyable interface.

```cs
class ___ ___ ___
```

*WorkerBee |
: |
IFlyable*

```cs
class WorkerBee : IFlyable
```

10. Pick the true statement.

- A base class inherits from a derived class.
- **A derived class inherits from a base class.**
- A base class inherits from a superclass.
- A superclass inherits from a subclass.

# 7/10 | 70%