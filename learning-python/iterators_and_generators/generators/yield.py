# Generator functions are similar to regular functions except that they must 
# return an iterator.
# But instead of using a return statement, generator functions use an expression
# called yield.
# So how does yield differ from a return statement? 
# Well, any code that is written after a yield expression will execute on the 
# next iteration of the iterator. Code written after a return statement will 
# not execute.

def course_generator():
  yield 'Computer Science'
  yield 'Art'
  yield 'Business'
  
courses = course_generator()
for course in courses:
    print(course)

# OUTPUT:  
# Computer Science
# Art
# Business

# Another key difference between yield and return is that the yield expression 
# will suspend the execution of the function and preserve any local variables
# that exist within the function. 
# The return statement will terminate the function immediately and return the
# result(s) to the caller.

# We want to create a generator that will generate values of class standings: 'Freshman', 'Sophomore', 'Junior', and 'Senior'. The generator function should be named class_standing_generator.
def class_standing_generator():
  yield "Freshman"
  yield "Sophomore"
  yield "Junior"
  yield "Senior"

class_standings = class_standing_generator()
for standing in class_standings:
  print(standing)

# OUTPUT:
# Freshman
# Sophomore
# Junior
# Senior