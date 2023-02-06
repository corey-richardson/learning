#There are some cases where it is useful to connect multiple generators into one.
# This allows us to delegate the operations of one generator to another 
# sub-generator. 
# Connecting generators is similar to using the itertools chain() function to
# combine iterators into a single iterator.

# In order to connect generators, we use the yield from statement.

def cs_courses():
    yield 'Computer Science'
    yield 'Artificial Intelligence'
 
def art_courses():
    yield 'Intro to Art'
    yield 'Selecting Mediums'
 
 
def all_courses():
    yield from cs_courses()
    yield from art_courses()
 
combined_generator = all_courses()

# We have a generator function called cs_courses() that yields two results, 
# 'Computer Science' and 'Artificial Intelligence'.
# We have another generator function called art_courses() that will yield two 
# separate results, 'Intro to Art' and 'Selecting Mediums'.
# Our all_courses() generator function will yield results from both cs_courses()
# and art_courses() to create one combined generator with all four string values
# representing the courses.

# Our printouts will look like the following:
# Computer Science
# Artificial Intelligence
# Intro to Art
# Selecting Mediums

# ---

# We have a generator function called science students(x) that yields science 
# major students with student IDs 1 to x. We have another generator function, 
# non_science_students(x,y), that yields non-science major students with 
# student IDs x-y. We want to retrieve student ids in the following order:
# Science students with IDs 1-5
# Non-science students with IDs 10-15
# Non-science students with IDs 25-30

# Use a connected generator function called combined_students that uses yield 
# from statements to achieve this.

def science_students(x):
  for i in range(1,x+1):
    yield i

def non_science_students(x,y):
  for i in range(x,y+1):
    yield i
  
def combined_students():
  yield from science_students(5)
  yield from non_science_students(10, 15)
  yield from non_science_students(25, 30)

# Call the combined_students() combined generator function and set it to a 
# variable named student_generator.
student_generator = combined_students()
for student in student_generator:
  print(student)