# Rover Control Center
Welcome to SPACE: Space Program for Aeronautical Collection and Exploration. You are in charge of the Rover Control Center. All rovers on Moon and Mars are under your direction!

This project will show you some ways in which references, inheritance, interfaces, and arrays can help you be a better C# programmer.

When you start this project you don’t need to read through the class definitions. In fact, the project will tell you when you need to look. To start, all you need to know is that MarsRover and MoonRover inherit from Rover:

```cs
class MoonRover : Rover

class MarsRover : Rover
```

Let’s get started!

#### Working with Rovers

1. 
There are two Moon rovers and one Mars rover defined in Program.cs. (We can ignore the satellite object for now.) To manage them all at once, we’ll need to put them in an array.

Store the three rovers in an array of type Rover[], their shared base class.

2.
You’ll regularly need to direct the rovers to send info, explore their surroundings, and collect samples.

Below Main(), write a static method DirectAll() that takes one argument of type Rover[]. The method should call the below three methods for each element and print out the returned strings.

GetInfo()
Explore()
Collect()

3.
Back in Main(), call the DirectAll() method using the array as the argument.

Make sure that the right text is printed to the screen!

4.
The leaders of SPACE have promoted you to Director of Probes! You are now in charge of all space probes, not just rovers.

To manage all space probes, which includes the three rovers and one satellite, put them in an array.

At the moment, the only inherited class they share is Object.

5.
To test that we built the Object[] array correctly, print the results of GetType() for each object in the array.

For clarity, use string interpolation to print something like “Tracking a [TYPE]…” for each one.

GetType() is one of the methods defined in Object, but it returns the actual type of the object, not the reference type. You can confirm this in the documentation.

#### Adding a Shared Interface

6.
As the SPACE Director of Probes, the Object array isn’t very useful because you can’t direct the probes to keep collecting and exploring!

We’ll need to create another shared class or interface. We have two options:

Create a superclass Probe that Rover and Satellite inherit from
Create an interface IDirectable that Rover and Satellite implement
The first option would involve a lot of changes to Rover and Satellite, like moving methods out of Rover and Satellite and into Probe or making those methods override.

It will be easier to just create a shared interface, which doesn’t require writing or changing any methods.

In IDirectable.cs, define an interface IDirectable with three methods:

string GetInfo()
string Explore()
string Collect()

7.
Edit Rover.cs and Satellite.cs so that they explicitly implement IDirectable.

8.
With a shared interface, we can manage Rover and Satellite types in the same array.

Back in Program.cs, create an array of type IDirectable[] containing all the probes (three rovers and one satellite).

9.
Update the DirectAll() method so that it now accepts one argument of type IDirectable[].

Try calling it with the newly created array!