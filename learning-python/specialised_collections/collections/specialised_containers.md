# Introduction to Specialised Containers

Now that we’ve had a refresher on some of the built-in containers Python provides, let’s dive into the collections module.

The classes from the collections module are very similar to the built-in containers we’ve been already using, but they contain new methods and utilities. Each of these specialized containers focuses on a certain improvement to its built-in counterpart such as optimizing performance, better organization, fewer steps for performing tasks, and more!

In order to use classes from the collections module, we will first need to import the module into our code. This is different than the previous containers we’ve seen because they were built-in and did not require an import.

Here are some of the various ways importing will look like:

```py
# To import a single class or multiple classes
from collections import name_of_class, name_of_another_class
 
# To import all classes in the collections module
from collections import *
 
# Another way to import all classes in a module
import collections
```

For a more specific example, here is what importing the OrderedDict (one of the specialized containers) would look like. We will dive deeper into the details of this particular container later on in this lesson but for now just observe the syntax:

```py
from collections import OrderedDict
 
orders = OrderedDict({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99},
          'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
 
orders.move_to_end('order_4829')
orders.popitem()
```

You might have noticed that this is a similar example to the dictionary review in the last exercise, but there are some new methods that provide even more functionality to the traditional dictionary.

Here is a list of all of the advanced containers we will be looking at in this lesson:

**Advanced Containers**
- deque
- namedtuple
- Counter
- defaultdict
- OrderedDict
- ChainMap

**Container Wrappers**
- UserDict
- UserList
- UserString

---

Let’s review the use case for each of the advanced containers from the collections class:

- deque
    - An advanced container which is optimized for appending and popping items from the front and back. For accessing many elements positioned elsewhere, it is better to use a list.
- namedtuple
    - The namedtuple lets us create an immutable data structure similar to a tuple, but we don’t have to access the stored data using indices. Instead, we can create instances of our namedtuple with named attributes. We can then use the . operator to retrieve data by the attribute names.
- Counter
    - This advanced container automatically counts the data within a hashable object which we pass into it’s constructor. It stores it as a dictionary where the keys are the elements and the values are the number of occurrences.
- defaultdict
    - An advanced container which behaves like a regular dictionary, except that it does not throw an error when trying to access a key which does not exist. Instead, it creates a new key:value pair where the value defaults to what we provide in the constructor for the defaultdict.
- OrderedDict
    - The OrderedDict combines the functionality of a list and a dict by preserving the order of elements, but also allowing us to access values using keys without having to provide an index for the position of stored dictionaries.
- ChainMap
    - This interesting container combines multiple mappings into a single container. When accessing a value using a key, it will search through every mapping contained within until a match is found or the end is reached. It also provides some useful methods for grouping parent and child mappings.
- UserDict
    - This is a container wrapper which lets us create our own version of a dictionary
- UserList
    - This is a container wrapper which lets us create our own version of a list
- UserString
    - This is a container wrapper which lets us create our own version of a string