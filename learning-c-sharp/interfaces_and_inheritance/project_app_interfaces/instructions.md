App Interfaces

The team at Computron Computing has asked you to join their product team to develop the hottest new Computron computer. You’ll be responsible for building some of the standard apps on this new machine, specifically the to-do list and the password manager.

At this point in development you have two classes started: TodoList representing the to-do list application and PasswordManager representing the password manager. In order to work within the Computron system, every app must have a display and reset feature. In other words, each class will need to implement the IDisplayable and IResetable interfaces.

Classes can implement multiple interfaces using the colon and comma syntax:

```cs
class TodoList : IDisplayable, IResetable
{}
```

Let’s get started! Make sure to save every file and test your code in the console with the command:

```
dotnet run
```

---

1.

Get comfortable with the two classes TodoList and PasswordManager. You can see in Program.cs an instance of each class constructed.

In TodoList.cs, read the definition of the constructor and Add() method

In PasswordManager.cs, read the definition of the constructor

IDisplayable

2.

Every app must have a display feature. In IDisplayable.cs, define an empty IDisplayable interface.

3.

Within IDisplayable declare one method that:

is named Display()

returns nothing

4.

In TodoList.cs, declare that the class implements the IDisplayable interface.

5.

The class must actually implement the interface by defining a Display() method.

Define a method that:

satisfies the interface requirements

uses Console.WriteLine() to write each to-do item to the console

6.

Repeat the process for PasswordManager.

Declare that it implements IDisplayable.

7.

Define a Display() method that:

satisfies the interface requirements

uses Console.WriteLine() to print the actual password if Hidden is false. If Hidden is true, print asterisks *

8.

Make sure that both classes are printable.

In Program.cs, call Display() on tdl and pm. Run the program with:

dotnet run

You should see both objects printed to the console.

IResetable

9.

Every app must have a reset feature. In IResetable.cs, define an IResetable interface with one method:

name it Reset()

it should return nothing

10.

In TodoList.cs, implement the interface:

Declare that it implements IResetable

Define a Reset() method to satisfy the interface. It should set the Todos property to an empty array of length 5 and set nextOpenIndex to 0.

11.

In PasswordManager, implement the interface:

Declare that it implements IResetable

Define a Reset() method to satisfy the interface. It should set Password to an empty string and set Hidden to false.

12.

In Program.cs, call Reset() and Display() with tdl and pm. In other words, both objects should display, then reset, then display again.

Run the program with:

dotnet run