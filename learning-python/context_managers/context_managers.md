A context manager is an object that takes care of the assigning and releasing of resources (files, database connections, etc).

- Preventing resource leaks
- Preventing crashes
- Decreasing the vulnerability of our data
- Preventing program slow-down.

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