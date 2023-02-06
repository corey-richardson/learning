# The generator method .close() is used to terminate a generator early. 
# Once the .close() method is called the generator is finished just like the 
# end of a for loop. Any further iteration attempts will raise a 
# StopIteration exception.

# next(my_generator)
# my_generator.close()
# next(my_generator) # raises StopGenerator exception

# The .close() method works by raising a GeneratorExit exception inside the 
# generator function. 
# The exception is generally ignored but can be handled using try and except.

# def generator():
#   i = 0
#   while True:
#     try:
#       yield i
#     except GeneratorExit:
#       print("Early exit, BYE!")
#       break
#     i += 1
#
# my_generator = generator()
# for item in my_generator:
#   print(item)
#   if item == 1:
#     my_generator.close()

# OUTPUT:
# 0
# 1
# Early exit, BYE!

# Putting the yield expression in a try block we can handle the GeneratorExit
# exception.

# ---

# We have a collection of 5,000 students. 
# We only want to retrieve information on the first 100 students. 
# Use the close() method to terminate the generator after 100 students.

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  if student_id >= 100:
    student_generator.close()