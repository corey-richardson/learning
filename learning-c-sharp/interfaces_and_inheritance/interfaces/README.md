In C#, an interface contains definitions for a group of related functionalities that a class can implement.

Interfaces are useful because they guarantee how a class behaves. This, along with the fact that a class can implement multiple interfaces, helps organize and modularize components of software.

**It is best practice to start the name of an interface with “I”.**

```cs
interface IAutomobile
{
  string LicensePlate { get; }
  double Speed { get; }
  int Wheels { get; }
}

// The IAutomobile interface has three properties. Any class that implements this interface must have these three properties.

public interface IAccount
{
  void PayInFunds ( decimal amount );
  bool WithdrawFunds ( decimal amount );
  decimal GetBalance ();
}

// The IAccount interface has three methods to implement.

public class CustomerAccount : IAccount
{ }

// This CustomerAccount class is labeled with : IAccount, which means that it will implement that interface.

```

---

In this lesson we’ll dive into interfaces, which are sets of actions and values that describe how a class can be used. This lets the computer check that we are using each type legally, thus preventing a whole group of type errors!

In this lesson you’ll learn how to:

- build your own interface
- write classes that implement an interface

---

The skeleton of an interface looks a bit like a class:

```cs
interface ISkellyBones
{
}
```

Every interface should have a name starting with “I”. This is a useful reminder to other developers and our future selves that this is an interface, not a class.

We can add members, like properties and methods, to the interface. Here’s an example of a fake property and method:

```cs
interface IAutomobile
{
  string Id { get; }
  void Vroom();
}
```

Notice that the property and method bodies are not defined. An interface is a set of actions and values, but it doesn’t specify how they work.

In our highway example, the highway patrol doesn’t care **HOW** the license plate property and honk method work, they just care **whether** every automobile has it.

---

As we design our automobile-like classes, we’ll need to implement this IAutomobile interface. In C#, we must first clearly announce that a class implements an interface using the colon syntax:

```cs
class Sedan : IAutomobile
{
  public string LicensePlate
  { get; }
 
  // and so on...
}
```

Remember that these members must be public. How else will the highway patrol be able to access them?