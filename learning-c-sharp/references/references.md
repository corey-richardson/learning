# References

## Cheatsheet Notes

- [C# Reference Types](#c-reference-types)
- [C# Object Reference](#c-object-reference)
- [C# Object Reference Functionality](#c-object-reference-functionality)
- [C# Polyphormism](#c-polyphormism)
- [C# Upcasting](#c-upcasting)
- [C# Downcasting](#c-downcasting)
- [C# Null Reference](#c-null-reference)
- [C# Value Types](#c-value-types)
- [C# Comparison Type](#c-comparison-type)
- [C# Override](#c-override)
- [C# Object Class](#c-object-class)
- [C# Object Class Methods](#c-object-class-methods)
- [C# ToString() Method](#c-tostring-method)
- [C# String Comparison](#c-string-comparison)
- [C# String Types Immutable](#c-string-types-immutable)
- [C# Empty String](#c-empty-string)

## Lesson Notes

- [References of the Same Type](#references-of-the-same-type)
- [References vs. Values](#references-vs-values)
- [References vs. Values Comparison](#references-vs-value-comparison)
- [References of Different Types](#references-of-different-types)
- [Arrays of References](#arrays-of-references)
- [Polymorphism](#polymorphism)
- [Casting](#casting)
- [Null and Unassigned References](#null-and-unassigned-references)

---

# Cheatsheet Notes

## C# Reference Types

In C#, classes and interfaces are reference types. Variables of reference types store references to their data (objects) in memory, and they do not contain the data itself.

An object of type `Object`, `string`, or `dynamic` is also a reference type.

```cs
SportsCar sc = new SportsCar(100);
SportsCar sc2 = sc;
sc.SpeedUp(); // Method adds 20
Console.WriteLine(sc.Speed); // 120
Console.WriteLine(sc2.Speed); // 120

// In this code, sc and sc2 refer to the same object. The last two lines will 
// print the same value to the console.
```

--- 

## C# Object Reference

In C#, an object may be referenced by any type in its inheritance hierarchy or by any of the interfaces it implements.

```cs
// Woman inherits from Human, which inherits from Animal, and it implements IPerson:
class Human : Animal
class Woman : Human, IPerson

// All of these references are valid:
Woman eve = new Woman();
Human h = eve;
Animal a = eve;
IPerson p = eve;
```

---

## C# Object Reference Functionality

In C#, the functionality available to an object reference is determined by the reference???s type, not the object???s type.

```cs
Player p = new Player();
Fan f = p;
p.SignContract();
f.SignContract();
// Error! 'SignContract()` is not defined for the type 'Fan'
```

---

## C# Polyphormism

Polymorphism is the ability in programming to present the same interface for different underlying forms (data types).

We can break the idea into two related concepts. A programming language supports polymorphism if:

- Objects of different types have a common interface (interface in the general meaning, not just a C# interface), and
- The objects can maintain functionality unique to their data type

```cs
class Novel : Book
{
  public override string Stringify()
  {
    return "This is a Novel!;
  }
}

class Book
{
  public virtual string Stringify()
  {
    return "This is a Book!;
  }
}

/* In the below code, you???ll see that a Novel and Book object can both be 
referred to as Books. This is one of their shared interfaces. At the same time,
they are different data types with unique functionality. */

Book bk = new Book();
Book warAndPeace = new Novel();
Console.WriteLine(bk.Stringify());
Console.WriteLine(warAndPeace.Stringify());

// This is a Book!
// This is a Novel

/* Even though bk and warAndPeace are the same type of reference, their 
behavior is different. Novel overrides the Stringify() method, so all Novel 
objects (regardless of reference type) will use that method. */
```

---

## C# Upcasting

In C#, upcasting is creating an inherited superclass or implemented interface reference from a subclass reference.

```cs
// In this case, string inherits from Object:

string s = "Hi";
Object o = s;

// In this case, Laptop implements the IPortable interface:

Laptop lap = new Laptop();
IPortable portable = lap;
```

---

## C# Downcasting

In C#, downcasting is creating a subclass reference from a superclass or interface reference.

Downcasting can lead to runtime errors if the superclass cannot be cast to the specified subclass.

```cs
Account a = new Account();
CustomerAccount ca = a;
// error CS0266: Cannot implicitly convert type `Account` to `CustomerAccount`. 
// An explicit conversion exists (are you missing a cast?)
```

```cs
// Dog inherits from Pet. An implicit downcast throws a compile-time error:
Pet pet = new Pet();
Dog dog = pet;
// error CS0266: Cannot implicitly convert type `Pet` to `Dog`. 
// An explicit conversion exists (are you missing a cast?)

// Every downcast must be explicit, using the cast operator, like (TYPE). 
// This fixes the compile-time error but raises a new runtime error.
Pet pet = new Pet();
Dog dog = (Pet)pet;
// runtime error: System.InvalidCastException: Specified cast is not valid.

//The explicit downcast would only work if the underlying object is of type Dog:
Dog dog = new Dog();
Pet pet = dog;
Dog puppy = (Dog)pet;
```

---

## C# Null Reference

In C#, an undefined reference is either a null reference or unassigned. A null reference is represented by the keyword null.

Be careful when checking for null and unassigned references. We can only compare a null reference if it is explicitly labeled null.

```cs
MyClass mc; //unassigned

Console.WriteLine (mc == null);
// error CS0165: Use of unassigned local variable 'mc'

MyClass mc = null; //explicitly 'null'

Console.WriteLine(mc == null);
// Prints true.

// Array of unassigned references
MyClass[] objects = new MyClass[5];
// objects[0] is unassigned, objects[1] is unassigned, etc...
```

---

## C# Value Types

In C#, value types contain the data itself. They include int, bool, char, and double.

Here???s the entire list of value types:

- char, bool, DateTime
- All numeric data types
- Structures (struct)
- Enumerations (enum)

---

## C# Comparison Type

In C#, the type of comparison performed with the equality operator (==), differs with reference and value types.

When two value types are compared, they are compared for value equality. They are equal if they hold the same value.

When two reference types are compared, they are compared for referential equality. They are equal if they refer to the same location in memory.

```cs
// int is a value type, so == uses value equality:
int num1 = 9;
int num2 = 9;
Console.WriteLine(num1 == num2);
// Prints true

// All classes are reference types, so == uses reference equality:
WorldCupTeam japan = new WorldCupTeam(2018);
WorldCupTeam brazil = new WorldCupTeam(2018);
Console.WriteLine(japan == brazil);
// Prints false
// This is because japan and brazil refer to two different locations in memory 
// (even though they contain objects with the same values):
```

---

## C# Override

In C#, the override modifier allows base class references to a derived object to access derived methods.

In other words: If a derived class overrides a member of its base class, then the overridden version can be accessed by derived references AND base references.

```cs
// In the below example, DerivedClass.Method1() overrides BaseClass.Method1(). 
// bcdc is a BaseClass-type reference to a DerivedClass value. 
// Calling bcdc.Method1() invokes DerivedClass.Method1().

class MainClass {
  public static void Main (string[] args) {
    BaseClass bc = new BaseClass();
    DerivedClass dc = new DerivedClass();
    BaseClass bcdc = new DerivedClass();

    bc.Method1();
    dc.Method1();
    bcdc.Method1();
  }
}

class BaseClass  
{  
    public virtual void Method1()  
    {  
        Console.WriteLine("Base - Method1");  
    }  
}  

class DerivedClass : BaseClass  
{  
    public override void Method1()  
    {  
        Console.WriteLine("Derived - Method1");  
    }  
}  

// The above code produces this result:
// Base - Method1
// Derived - Method1
// Derived - Method1

// If we wanted bcdc.Method1() to invoked BaseClass.Method1(), 
// then we would label DerivedClass.Method1() as new, not override.
```

---

## C# Object Class

In C#, the base class of all types is the Object class. Every class implicitly inherits this class.

When you create a class with no inheritance, C# implicitly makes it inherit from Object.

```cs
// When you write this code:
class Dog {}
// C# assumes you mean:
class Dog : Object {}

/* Even if your class explicitly inherits from a class that is NOT an Object, 
then some class in its class hierachy will inherit from Object. 
In the below example, Dog inherits from Pet, which inherits from Animal, 
which inherits from Object: */
class Dog : Pet {}
class Pet : Animal {}
class Animal {}

// Since every class inherits from Object, 
// any instance of a class can be referred to as an Object.
Dog puppy = new Dog();
Object o = puppy;
```

---

## C# Object Class Methods

In C#, the Object class includes definitions for these methods: ToString(), Equals(Object), and GetType().

```cs
Object obj = new Object();
Console.WriteLine(obj.ToString());
// The example displays the following output:
//      System.Object

public static void Main()
{
	MyBaseClass myBase = new MyBaseClass();
  MyDerivedClass myDerived = new MyDerivedClass();
  object o = myDerived;
  MyBaseClass b = myDerived;

	Console.WriteLine("mybase: Type is {0}", myBase.GetType());
  Console.WriteLine("myDerived: Type is {0}", myDerived.GetType());
  Console.WriteLine("object o = myDerived: Type is {0}", o.GetType());
  Console.WriteLine("MyBaseClass b = myDerived: Type is {0}", b.GetType());
}

// The example displays the following output:
//    mybase: Type is MyBaseClass
//    myDerived: Type is MyDerivedClass
//    object o = myDerived: Type is MyDerivedClass
//    MyBaseClass b = myDerived: Type is MyDerivedClass
```

---

## C# ToString() Method
When a non-string object is printed to the console with Console.WriteLine(), its ToString() method is called.

```cs
Random r = new Random();

// These two lines are equivalent:
Console.WriteLine(r);
Console.WriteLine(r.ToString());
```

---

## C# String Comparison

In C#, string is a reference type but it can be compared by value using ==.

```cs
//In this example, even if s and t are not referentially equal, 
// they are equal by value:
string s = "hello";
string t = "hello";

// b is true
bool b = (s == t);
```

--- 

## C# String Types Immutable

In C#, string types are immutable, which means they cannot be changed after they are created.

```cs
/* Two examples demonstrating how immutablility determines string behavior. 
In both examples, changing one string variable will not affect other 
variables that originally shared that value. */

//EXAMPLE 1
string a = "Hello?";
string b = a;
b = "HELLLLLLLO!!!!";

Console.WriteLine(b);
// Prints "HELLLLLLLO!!!!"

Console.WriteLine(a);
// Prints "Hello?"


//EXAMPLE 2
string s1 = "Hello ";
string s2 = s1;
s1 += "World";

System.Console.WriteLine(s2);
// Prints "Hello "
```

---

## C# Empty String

In C#, a string reference can refer to an empty string with "" and String.Empty.

This is separate from null and unassigned references, which are also possible for string types.

```cs
// Empty string:
string s1 = "";

// Also empty string:
string s2 = String.Empty;

// This prints true:
Console.WriteLine(s1 == s2);

// Unassigned:
string s3;

// Null:
string s4 = null;
```

---

# Lesson Notes

## References of the Same Type

- [references_of_the_same_type.cs](/learning-c-sharp/references/reference_fundamentals/references_of_the_same_type.cs)

Classes are *reference types*. That means that when we create a new instance of a class and store it in a variable, the variable is a *reference* to the object.

Let???s see what???s happening behind the scenes. When this code is run:

```cs
Dissertation diss1 = new Dissertation();
```

A new `Dissertation` instance is constructed and stored in the computer???s memory. You can imagine a slot in your computer holding the instance???s type, property values, etc. `diss1` is a reference to that location in memory.

`diss1` is not the actual object, it is a *reference* to the object. Thus an object can have multiple references:

```cs
Dissertation diss1 = new Dissertation();
Dissertation diss2 = diss1;
```

Now there are two references to the same location in memory: we can say that `diss1` and `diss2` refer to the same object. If changes are made to that object, then they will be reflected in both references to it:

```cs
Dissertation diss1 = new Dissertation();
Dissertation diss2 = diss1;
diss1.CurrentPage = 0;
diss2.CurrentPage = 16;
Console.WriteLine(diss1.CurrentPage);
Console.WriteLine(diss2.CurrentPage);
```

- The middle two lines of this code are setting the `CurrentPage` property of the same object (first setting it to `0`, then `16`)
- The last two lines will print the same value, `16`

You can imagine references like directions to a house: they tell you where to find the house, but they are not the house itself!

--- 

## References vs. Values

- [references_vs_values.cs](/learning-c-sharp/references/reference_fundamentals/references_vs_values.cs)

To better grasp the idea of reference types, let???s look at the other kind of type: *value types*. While reference-type variables refer to a place in memory, value-type variables hold the actual data.

`int` is a value type, so the variable `num` holds the value `6`:

```cs
int num = 6;
```

Reference types, on the other hand, refer to a location in memory. Every class is a reference type, so the variable `diss` refers to a location in memory that has the `Dissertation` object:

```cs
Dissertation diss = new Dissertation(50);
```

Every ???primitive??? data type is a value type, including:

- int
- double
- bool
- char

Revisiting our metaphor: a reference is like directions to a house, which ???points??? to a house. It isn???t the actual house. A value type is the house itself!

You might have noticed that ```string``` is missing here. It works a bit differently, so it will be covered in a later lesson.

While reference-type variables refer to a place in memory, value-type variables hold the actual data.

---

## References vs. Value Comparison

- [references_vs_value_comparison.cs](/learning-c-sharp/references/reference_fundamentals/references_vs_value_comparison.cs)

When we compare value types with ==, the C# compiler performs a value comparison. For example, this prints true because the value 6 is equal to the value 6:

```cs
int int1 = 6;
int int2 = 6;
Console.WriteLine(int1 == int2);
// Output: true
```

int1 and int2 are the actual value 6. When we compare the value 6 with 6, they???re the same!

When we compare reference types with `==`, the C# compiler performs a *referential* comparison, which means it checks if two variables refer to the same memory location. For example, this prints false because d1 and d2 refer to two different locations in memory (even though they contain objects with the same values):

```cs
Dissertation d1 = new Dissertation(50);
Dissertation d2 = new Dissertation(50);
Console.WriteLine(d1 == d2);
// Output: false
```

We constructed two different Dissertation objects which happened to have the same values. Each reference (d1 and d2) point to different objects, so they are not equal.

## References of Different Types

- [references_of_different_types](/learning-c-sharp/references/reference_fundamentals/references_of_different_types/)
- [Program.cs](/learning-c-sharp/references/reference_fundamentals/references_of_different_types/Program.cs)
- [Book.cs](/learning-c-sharp/references/reference_fundamentals/references_of_different_types/Book.cs)
- [IFlippable.cs](/learning-c-sharp/references/reference_fundamentals/references_of_different_types/IFlippable.cs)

Before going any further, let???s remind ourselves that `Dissertation` implements `IFlippable`, which has the `CurrentPage` property and `Flip()` method. You???ll need this info in a minute.

In our previous example both references to the Dissertation object were of type Dissertation:

```cs
Dissertation diss1 = new Dissertation();
Dissertation diss2 = diss1;
```

Whenever we use diss1 and diss2 we can handle the Dissertation object as if it were a Dissertation type. Since Dissertation also implements the IFlippable interface, we can reference it that way too:

```cs
Dissertation diss = new Dissertation(50);
IFlippable fdiss = diss;
```

Now diss and fdiss refer to the same object, but fdiss is an IFlippable reference, so it can ONLY use IFlippable functionality:

```cs
diss.Flip();
fdiss.Flip();
Console.WriteLine(diss.Define());
// This causes an error!
Console.WriteLine(fdiss.Define());
```

This last line causes an error because Define() is not a method in the IFlippable interface. The other lines do NOT cause errors because they use members that both IFlippable and Dissertation have.

This rule also applies to base classes too, so we can refer to a Dissertation object as Book.

```cs
Dissertation diss = new Dissertation(50);
Book bdiss = diss;
Console.WriteLine(diss.Title);
Console.WriteLine(bdiss.Title);
diss.Define();
// This causes an error!
bdiss.Define();
```

Title is defined for Book, so no error is thrown there. Define(), however, is not defined for the Book class, so we can???t use it with Book references.

## Arrays of References

- [arrays_of_references.cs](/learning-c-sharp/references/reference_fundamentals/arrays_of_references.cs)

We know that we can use inherited classes and implemented interfaces to reference an object:

Dissertation diss = new Dissertation(50);
IFlippable fdiss = diss;
This allows us to work with many similar types at the same time. Imagine if we didn???t have this feature and we had to ???flip??? a group of Diary and Dissertation types:

```cs
Diary dy1 = new Diary(1);
Diary dy2 = new Diary(30);
Dissertation diss1 = new Dissertation(50);
Dissertation diss2 = new Dissertation(49);
dy1.Flip();
dy2.Flip();
diss1.Flip();
diss2.Flip();
```

Look at all that code! It would be faster and safer if we could store the references in an array and loop through it. But would it be an array of Diary[] or an array of Dissertation[] or something else? Since both dissertations and diaries are flippable (they both implement the IFlippable interface), we can create references to them as IFlippables:

```cs
IFlippable f1 = new Diary(1);
IFlippable f2 = new Diary(30);
IFlippable f3 = new Dissertation(50);
IFlippable f4 = new Dissertation(49);
```

Instead of dealing with individual variables, we can use an array of IFlippable references:

```cs
IFlippable[] classroom = new IFlippable[] { new Diary(1), new Diary(30), new Dissertation(50), new Dissertation(49) };
```

Then to ???flip??? each element, we can write a foreach loop:

```cs
foreach (IFlippable f in classroom) 
{
  f.Flip();
}
```

We can only access the functionality defined in the interface. For example, we couldn???t access f.Title because Title isn???t a property defined in IFlippable.

## Polymorphism

- [polymorphism](/learning-c-sharp/references/reference_fundamentals/polymorphism/)
- [Program.cs](/learning-c-sharp/references/reference_fundamentals/polymorphism/Program.cs)
- [Book.cs](/learning-c-sharp/references/reference_fundamentals/polymorphism/Book.cs)
- [Diary.cs](/learning-c-sharp/references/reference_fundamentals/polymorphism/Diary.cs)

We just saw how useful it is to have the same interface for multiple data types. This is a common concept across many programming languages, and it???s called polymorphism.

The concept really includes two related ideas. A programming language supports polymorphism if:

- Objects of different types have a common interface (interface in the general meaning, not just a C# interface), and
- The objects can maintain functionality unique to their data type

Let???s prove to ourselves that this is true in C#. We???ll use the example of Stringify: Dissertation and Book have different Stringify() methods but can both be referenced as Books.

Here are snippets from each class:

```cs
class Dissertation : Book
{
  public override string Stringify()
  {
    return "This is a Dissertation object!";
  }
}

class Book
{
  public virtual string Stringify()
  {
    return "This is a Book object!";
  }
}
```
Given that information, what will the below program print?

```cs
Book bk = new Book();
Book bdiss = new Dissertation();
Console.WriteLine(bk.Stringify());
Console.WriteLine(bdiss.Stringify());
```

The answer is:

```
This is a Book object!
This is a Dissertation object!
```

Even though bk and bdiss are both Book type references, their behavior is different. Dissertation overrides the Stringify() method, so all Dissertation objects (regardless of reference type) will use that method.

Therefore, C# support polymorphism!

You???ll never have to write polymorphism in your code, but this vocabulary is essential to communicating with other developers!

**So remember: polymorphism is the ability in programming to present the same interface for differing data types.**

## Casting

- [casting.cs](/learning-c-sharp/references/reference_fundamentals/casting.cs)

So far we???ve referred to objects with a reference of their own type, an inherited type, or an implemented interface:

```cs
Dissertation diss = new Dissertation();
Book bdiss = diss;
IFlippable fdiss = diss;
```

The process is called *upcasting*. As we saw in the last exercise upcasting allows us to work with multiple types at once. It also lets us safely store an object without knowing its specific type. You can think of upcasting as using a reference ???up??? the inheritance hierarchy.

What happens if you try to *downcast*, or reference an object by a subclass? You???ll need to do this when you want to access the specific functionality of a subclass.

For example what happens when we refer to a Book object as a Dissertation type?

```cs
Book bk = new Book();
Dissertation dbk = bk;
// Error!
```

The code produces this error:

```
error CS0266: Cannot implicitly convert type `Book` to `Dissertation`. 
An explicit conversion exists (are you missing a cast?)
```

Not every downcast is possible in C#. In this case, Dissertation has a Define() method that is incompatible with Book. This is the computer???s way of telling you: there???s a chance that this cast won???t work!

To get around this error, we must explicitly downcast, like below. The desired type is written in parentheses:

```cs
Book bk = new Book();
Dissertation bdk = (Dissertation)bk;
```

This essentially tells the computer: ???I know the risk I???m taking, and this might fail if I???m not careful.???

In many cases, the downcast will still fail. Here, the Dissertation type reference bdk can???t reference a Book object, so when we explicitly downcast we see that it fails with a new error message:

```
System.InvalidCastException: Specified cast is not valid.
```

There are multiple ways to deal with downcasting, including the as and is operators. We won???t get into those now, but you can learn about them in the Microsoft C# Programming Guide: [Casting and type conversions](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/types/casting-and-type-conversions) if you???d like. For now, focus on these things:

- Upcasting is creating a superclass or interface reference from a subclass reference
- Downcasting is creating a subclass reference from a superclass or interface reference.
- Upcasting can be done implicitly, while downcasting cannot

## Null and Unassigned References

- [null_and_unassigned_references.cs](/learning-c-sharp/references/reference_fundamentals/null_and_unassigned_references.cs)

So far we???ve seen:

- A reference to an object
- Multiple references to an object

**What about a reference that refers to no object?**

In C# a reference to no object is called either a null reference or unassigned. We???ll need to apply these concepts in C# whenever we want to show that a reference is ???missing???, create a reference variable without defining it, or initialize an empty array.

In the first use case, we???d like to create a reference that is ???missing??? or empty. We set it equal to the keyword null:

```cs
Diary dy = null;
```

In the second case, if we create a reference variable without a value, it is unassigned:

```cs
Diary dy;
// dy is unassigned
```

In the third case, if we create an empty array of reference types, each element is an unassigned reference:

```cs
Diary[] diaries = new Diary[5];
// diaries[1] is unassigned, diaries[2] is unassigned, etc.
```

Be careful when checking for null and unassigned references. We can only compare a null reference if it is explicitly labeled null:

```cs
Diary dy = null;
Console.WriteLine(dy == null);
// Output: true
```

For the other two cases, comparing an unassigned variable we???ll get an error:

```cs
Object o;
Console.WriteLine (o == null);
// error CS0165: Use of unassigned local variable 'o'
```

This might seem annoying at first, but it???s actually a good thing: the C# compiler prevents future issues down the road by raising an error the first time an unassigned variable is used.