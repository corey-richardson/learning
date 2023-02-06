In Python, a generator allows for the creation of iterators without having to implement __iter__() and __next__() methods. Generators improve code readability, save memory by allowing for iterative access of elements, and allow for the traversal of infinite streams of data.

There are two types of generators in Python:

Generator functions

Generator Expressions

Both of these return a generator object that can be looped over similar to a list, but unlike a list, the contents of the generator object are not stored in memory, allowing for complex and even infinite iteration of data.

Defining a generator function will resemble how we already define regular functions, except for a few key components that we will dive into in the following exercises.