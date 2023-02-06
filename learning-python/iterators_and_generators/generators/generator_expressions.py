# Generator expressions allow for a clean, single-line definition and creation
# of an iterator.
# By using a generator expression, there is no need to define a full generator
# function as we covered in the previous exercises.

# List comprehension
a_list = [i*i for i in range(4)]
# Generator comprehension
a_generator = (i*i for i in range(4))

print(a_list)
print(a_generator)

# [0, 1, 4, 9]
# <generator object <genexpr> at 0x7f82e0e4d4c0>

# Since our generator expression returns an iterator object, we can loop through
# to obtain the values within it:
for i in a_generator:
    print(i)
# 0 1 4 9

# ---

def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Given the defined generator function cs_generator(), retrieve a generator
# object by calling cs_generator() and set it to a variable called cs_courses.
cs_courses = cs_generator()
for course in cs_courses:
  print(course)

# After the for loop, create an iterator using a generator expression and put 
# it in a variable called cs_generator_exp. 
# The iterator should produce the same output as cs_generator().
cs_generator_exp = (f"Computer Science {i}" for i in range(1,5))
for course in cs_generator_exp:
  print(course)
  
# Computer Science 1
# Computer Science 2
# Computer Science 3
# Computer Science 4
# Computer Science 1
# Computer Science 2
# Computer Science 3
# Computer Science 4