# The generator method throw() provides the ability to throw an exception inside
# the generator from the caller point. 
# This can be useful if we need to end the generator once it reaches a certain
# value or meets a particular condition.

# def generator():
#   i = 0
#   while True:
#     yield i
#     i += 1
 
# my_generator = generator()
# for item in my_generator:
#     if item == 3:
#         my_generator.throw(ValueError, "Bad value given")
        
# ---

# We only want to retrieve information on the first 100 students. 
# Use the throw() method to throw a ValueError of “Invalid student ID” if the
# iterated student ID goes over 100. Insert your code before the 
# print(student_id) line.

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  if student_id > 100:
    student_generator.throw(ValueError,"Invalid student ID")
  print(student_id)

# 1
# 2
# 3
# ...
# 98
# 99
# 100
# Traceback (most recent call last):
#   File "script.py", line 10, in <module>
#     student_generator.throw(ValueError,"Invalid student ID")
#   File "script.py", line 5, in student_counter
#     yield i
# ValueError: Invalid student ID