# Generator functions return an iterator object that contains traversable values. 
# To retrieve the next value from a generator object, we can use the Python 
# built-in function next() which will cause the generator function to resume 
# its execution until the next yield expression is found. After the next yield
# expression is found, the function will pause execution again.
# If no additional yield expressions are found in a generator function, that 
# means the code has finished and a StopIteration is raised.

# Generator functions are not limited to just single yield statements. 
# They can also include loops where the yield occurs.
# To see this in action, imagine we have a dictionary of students and their 
# student ID numbers. We want to hold a raffle where every student whose student
# ID is a multiple of 3 wins prize A and every student whose ID is a multiple of
# 5 wins prize B. Any student whose ID is both a multiple of 3 and 5
# wins prize C.

def prize_generator():
  student_info = {
    "Joan Stark": 355,
    "Billy Mars": 45,
    "Tori Rivers": 18,
    "Kyle Newman": 25
  }
 
  for student in student_info:
    name = student
    id = student_info[name]
    if id % 3 == 0 and id % 5 == 0:
      yield student + " gets prize C"
    elif id % 3 == 0:
      yield student + " gets prize A"
    elif id % 5 == 0:
      yield student + " gets prize B"
      
# Since this is a generator function, the local variable dictionary, student_info
# is preserved while the function executes with each next() call.

prizes = prize_generator()
print(next(prizes))
print(next(prizes))
print(next(prizes))
print(next(prizes))

# Joan Stark gets prize B
# Billy Mars gets prize C
# Tori Rivers gets prize A
# Kyle Newman gets prize B

# If we were to call next() one additional time, we would see a StopIteration 
# exception raised since the student_info dictionary will have been exhausted.

# ---

def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  # Finish the function by adding a for loop that traverses through the 
  # student_standings list and yields 500 for each 'Freshman' value.
  for standing in student_standings:
    if standing == "Freshman":
      yield 500
  
# Outside the function, retrieve the iterator object by calling 
# student_standing_generator() and set it to a variable called standing_values.
# Print out the values within the returned standing_values generator using the
# Python built-in function next().
# Two values of 500 should be retrieved since our student_standings list 
# contained two 'Freshman' values.
standing_values = student_standing_generator()
print(next(standing_values))
print(next(standing_values))

# Use next() one more time on the generator object. 
# What occurs?

# print(next(standing_values))

# 500
# 500
# Traceback (most recent call last):
#   File "script.py", line 13, in <module>
#     print(next(standing_values))
# StopIteration