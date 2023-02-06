# The .send() method allows us to send a value to a generator using the 
# yield expression. 
# If you assign yield to a variable the argument passed to the .send() method 
# will be assigned to that variable.
# Calling .send() will also cause the generator to perform an iteration.

# def count_generator():
#   while True:
#     n = yield
#     print(n)
 
# my_generator = count_generator()
# next(my_generator) # 1st Iteration Output: 
# next(my_generator) # 2nd Iteration Output: None
# my_generator.send(3) # 3rd Iteration Output: 3
# next(my_generator) # 4th Iteration Output: None

# The 1st iteration creates no output since the execution stops at n = yield
# which is before print(n).
# The 2nd iteration assigns None to n through the n = yield expression. 
# None is printed.
# The 3rd iteration is caused by my_generator.send(3). The value 3 is passed 
# through yield and assigned to n. 3 is printed.
# The last, and 4th, iteration, assigns None to n. None is printed.

MAX_STUDENTS = 50

def get_student_ids():
    student_id = 1
    while student_id <= MAX_STUDENTS:
        # Change the yield expression so the value from yield is assigned to n.
        n = yield student_id
        # Just below the yield expression check that n is not equal to None. 
        # If they are not equal, assign the value of n to student_id.
        if n != None: # BEST PRACTICE: is not None, instead of != None
            student_id = n
            # Still inside the if statement, stop student_id from incrementing by
            # skipping the rest of the iteration.
            continue
    
        student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
    # Inside the for loop and before print(i):
    # Check if i is equal to the first id number, 1.
    # If so, set i to the return value of the student_id_generator.send() method.
    # Set the argument for the .send() method so the output starts at 25.
    if i == 1:
        i = student_id_generator.send(25)
    print(i)