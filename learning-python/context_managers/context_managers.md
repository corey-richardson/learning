A context manager is an object that takes care of the assigning and releasing of resources (files, database connections, etc).

- Preventing resource leaks
- Preventing crashes
- Decreasing the vulnerability of our data
- Preventing program slow-down.

## With statement

We already explored this concept when we used the with statement when operating on files. The with statement is the most common and pythonic way of invoking context managers in python.

```py
with open("file_name.txt", "w") as file:
   file.write("How you gonna win when you ain't right within?")
```

1. The with statement calls the built-in open() function on "file_name.txt" with a mode of "w" which represents write mode.
2. The as clause assigns the object opened (the file) to a target variable called file, which can be accessed inside of the context manager.
3. file.write() writes a sentence to "file_name.txt"

Here is what the same code would look like without the use of a context manager like with:

```py
file = open("file_name.txt", "w")
try:
   file.write("How you gonna win when you ain't right within?")
finally:
   file.close()
```

The alternative to using with would require us to manually open (using open()) and close (using close()) the file we are working on. By using the with statement in the first example, it serves as a context manager where files are automatically closed after script completion and we don’t ever have to worry about the possibility of forgetting to close a resource.

---

## Class based context manager

One of the two approaches of creating context managers is referred to as the class-based approach. The class-based approach of writing context managers requires explicitly defining and implementing the following two methods inside of a class:

- An __enter__ method
    - The __enter__ method allows for the setup of context managers. This method commonly takes care of opening resources (like files). This method also begins what is known as the runtime context - the period of time in which a script runs. In our previous examples, it was the time in which the code passed into the with statement code block was executed (basically everything under the with statement).

- An __exit__ method
    - The __exit__ ensures the breakdown of the context manager. This method commonly takes care of closing open resources that are no longer in use.

```py
class ContextManager:
  def __init__(self):
    print('Initializing class...')
 
  def __enter__(self):
    print('Entering context...')
 
  def __exit__(self, *exc):
    print('Exiting context...')
```

Here we invoke the ContextManager class with a with statement:

```py
with ContextManager() as cm:
  print('Code inside with statement')
```

After running the code, our output of this context manager would be:

    Initializing class...
    Entering context...
    Code inside with statement
    Exiting context...

1. `__init__` method
2. `__enter__` method
3. The code in the with statement block
4. `__exit__` method

---

Let’s walk through a context manager that manages actual files as well as explore each of the methods we saw earlier. Here is what our context manager will look like:

```py
class WorkWithFile:
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode

def __enter__(self):
  self.opened_file = open(self.file, self.mode)
  return self.opened_file

def __exit__(self, *exc):
  self.opened_file.close()
```

Now that we created our context manager, we can now use it in a with statement like so:

```py
with WorkWithFile("file.txt", "r") as file:
  print(file.read())
```

---

Within a context manager, the __exit__ method is responsible for dealing with any exceptions. It can implement how to close the file and any other operations we want to perform if an exception occurs.

The __exit__ method has three required arguments (in addition to self):

1. An exception type: which indicates the class of exception (i.e. AttributeError class, or NameError class)
2. An exception value: the actual value of the error
3. A traceback: a report detailing the sequence of steps that caused the error and all the details needed to fix the error.

```py
class OpenFile:
 
 def __init__(self, file, mode):
   self.file = file
   self.mode = mode
 
 def __enter__(self):
   self.opened_file = open(self.file, self.mode)
   return self.opened_file
 
 def __exit__(self, exc_type, exc_val, traceback):
   print(exc_type)
   print(exc_val)
   print(traceback)
   self.opened_file.close()

with OpenFile("file.txt", "r") as file:
  # .see() is not a real method
  print(file.see())
```

```
<class 'AttributeError'>
'_io.TextIOWrapper' object has no attribute 'see'
<traceback object at 0x7f08dcfb5040>
```

```
Traceback (most recent call last):
  File "script.py", line 14, in <module>
    print(file.see())
AttributeError: '_io.TextIOWrapper' object has no attribute 'see'
```

In contrast, if no error occurs in the with statement above, the __exit__ method would have printed:

    None
    None
    None