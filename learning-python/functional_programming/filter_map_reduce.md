The first function we will look at is `filter()`, which converts the following imperative code:

```py
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 
# filter_values is not a higher-order function
def filter_values(predicate, lst):
 
  # Mutable list required because this example is imperative, not declarative
  ret = []
  for i in lst:
    if predicate(i):
      ret.append(i)
  return ret
 
filtered_numbers = filter_values(lambda x: x % 2 == 0, nums) 
 
print(filtered_numbers) 
 
# This will output the list: [2, 4, 6, 8, 10]
```

into the following declarative code:

```py
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 
filtered_numbers = filter(lambda x: x % 2 == 0, nums) 
 
print(tuple(filtered_numbers))
 
# This will output the tuple: (2, 4, 6, 8, 10)
```

`map()` converts the following imperative code:

```py
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 
def mapper(function, lst):
  ret = []
  for i in lst:
    ret.append(function(i))
  return ret
 
mapped_numbers  = mapper(lambda x: x*x, nums)
 
print(tuple(mapped_numbers))
 
# This will output: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

Into the following declarative code:

```py
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 
mapped_numbers = map(lambda x: x*x, numbers) 
 
print(tuple(mapped_numbers))
 
# This will also output: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

The `reduce()` function accepts an iterable and a two-parameter function (no more than two) known as an *"accumulator"*. It uses the accumulator to recursively process the contents of the iterable and “reduce” them to one value. An example application of `reduce()` would be to compute the sum of all numbers in a list.

The sum of all elements in a tuple written imperatively:

```py
nums = (2, 6, 7, 9, 1, 4, 8)
 
sum = 0
 
for i in nums:
  sum += i
 
print(sum) # Output: 37
Using reduce() to find the sum declaratively:

"""
In Python 3, the `reduce()` function has been moved to the `functools` library, so we need 
to import it before we can use it.
"""
from functools import reduce
 
nums = (2, 6, 7, 9, 1, 4, 8)
 
reduced_nums = reduce(lambda x, y: x + y, nums) # reduced_nums is a number
 
print(reduced_nums) # Output: 37
```

The lambda in `reduce()` requires exactly two parameters.

Higher-order functions are powerful tools that you can use to significantly shorten code, thereby leading to cleaner and more concise solutions. In later exercises, we will explore how to combine these functions.

---

# Map
The map() higher-order function has the following base structure:

```py
returned_map_object = map(function, iterable)
```

When called, `map()` applies the passed function to each and every element in the iterable and returns a map object.

We will usually convert the map into a list to enable viewing and further use.

![map() function gif](https://static-assets.codecademy.com/Courses/Intermediate-Python/Map()-Function.gif)

```py
def double(x):
 return x*2
 
int_list = [3, 6, 9]
 
doubled = map(double, int_list)
 
print(doubled)
```

> `<map at 0x7f1ca0f58090>`

```py
print(list(doubled))
```

> `[6, 12, 18]`

Higher-order functions like map() work especially well with lambda functions. Because lambda functions are anonymous, we don’t need to define a new named function for map() if that function won’t be used again elsewhere.

```py
doubled = map(lambda input: input*2, int_list)
print(list(doubled))
```

> `[6, 12, 18]`

---

# Filter

Similar to map(), the filter() function takes a function and an iterable as arguments. Just as the name suggests, the goal of the filter() function is to “filter” values out of an iterable.

![filter](https://static-assets.codecademy.com/Courses/Intermediate-Python/Filter()-Function.gif)

a function that filters a collection of names and returns only the names that start with the letter M or m:

```py
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names) 
print(list(M_names))
```

> `['margarita', 'Masako', 'Maki']`

---

# Reduce

Lastly, we have the reduce() function, which has two distinct differences from the built-in higher-order functions that we have learned so far.
- In contrast to the map() and filter() functions that are always available, the reduce() function ***must be imported from the functools module*** to use it.
- Rather than returning a reduce object as might be expected after learning about map() and filter(), reduce() returns a single value. To get to this single value, reduce() cumulatively applies a passed function to each sequential pair of elements in an iterable.

![reduce](https://static-assets.codecademy.com/Courses/Intermediate-Python/Reduce()-Function.gif)

```py
from functools import reduce
 
int_list = [3, 6, 9, 12]
 
reduced_int_list = reduce(lambda x,y: x*y, int_list)
 
print(reduced_int_list)
```

> `1944` (3 * 6 * 9 * 12)

- The reduce() function takes 2 arguments: a lambda function and a list of integers.
- The lambda function takes 2 numbers, x and y and multiplies them together.
- The reduce() function applies the lambda function to the first two elements in the list, 3 and 6, to get a product of 18.
- Next, 18 was multiplied by the following element in the list, 9, to get 162.
- Continuing on, 162 was multiplied by the next element, 12, to get 1944.
- This last, final value—1944—is what was returned by reduce().