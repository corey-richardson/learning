# Python’s Itertools: Built-in Iterators

While building our own custom iterator classes can be useful, Python offers a convenient, built-in module named itertools that provides the ability to create complex iterator manipulations. These iterator operations can input either a single iterable or a combination of them.

There are three categories of itertool iterators:

- Infinite: Infinite iterators will repeat an infinite number of times. They will not raise a StopIteration exception and will require some type of stop condition to exit from.
- Input-Dependent: Input-dependent iterators are terminated by the input iterable(s) sequence length. This means that the smallest length iterable parameter of an input-dependent iterator will terminate the iterator.
- Combinatoric: Combinatoric iterators are iterators that are combinational, where mathematical functions are performed on the input iterable(s).

We can use the itertools module by simply supplying an import statement at the top of the module like this:

```py
import itertools
```
¬[](https://static-assets.codecademy.com/Courses/Intermediate-Python/Built-in-Iterators.svg)