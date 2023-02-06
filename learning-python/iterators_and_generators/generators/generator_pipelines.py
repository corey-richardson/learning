# Generator pipelines allow us to use multiple generators to perform a series
# of operations all within one expression.
# We can break down complex operations into smaller, more manageable parts
# where they can then be pipelined together to achieve the desired output.

# Pipeline generators are also often referred to as nested generators.

# We have three courses:
# Computer Science which has 5 students
# Art which has 10 students
# Business which has 15 students

# First, complete the generator function called course_generator that can
# yield tuples of (Course name, Number students) for the above courses and the
# corresponding number of students. The first tuple for Computer Science has 
# been provided.

def course_generator():
    yield ("Computer Science", 5)
    yield ("Art", 10)
    yield ("Business", 15)

# Create a generator function called add_five_students that takes in an input
# variable called courses. This courses object contains tuples of (Course name,
# Number of students). The add_five_students generator function should loop 
# through the courses input object.
# On each iteration, it should yield a tuple containing the course name and 
# number of students plus 5.  
def add_five_students(courses):
  for course, num_students in courses:
    # print(course)
    # print(num_students)
    yield (course, num_students + 5)

# Use a pipeline generator (nested generator) to get the resulting generator 
# that has the 5 added students to each course. Set it to a variable called 
# increased_courses.
increased_courses = add_five_students(course_generator())
for course in increased_courses:
  print(course)