def summa():
    yield 'Summa Cum Laude'
def magna():
    yield 'Magna Cum Laude' 
def cum_laude():
    yield 'Cum Laude'

# Create a generator function called graduation_countdown() that will countdown 
# the number of days left before student graduation.
# It should take in as input days and yield one less day on each next() call, 
# so the last value yielded is 0. 
# Use a while loop for yielding and decrementing the day.
def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left is not None:
      days = days_left
      continue
    else:
      days -= 1

days = 25
gpas = [3.2, 4.0, 3.6, 2.9]

# Create an equivalent generator expression called countdown_generator for the
# graduation_countdown generator function.
# It should generate the days in a descending order starting from the provided 
# days value.
# Place the code after the days = 25 line.
countdown_generator = (i for i in range(days, -1, -1))

# Modify the graduation_countdown() generator function to accept values sent 
# using send().
# Use a local variable called days_left to store sent values. 
# Use an if/else statement to check for sent values.

# Call the graduation_countdown() function and set it to a variable called 
# grad_days.
# Iterate through grad_days generator to print the number of days left with a 
# string of “Days Left: x” where x represents the countdown value.
# On the 15th day of the graduation countdown, the school president announces 
# that graduation will be moved up 5 days.
# Send a value of 10 to the grad_days generator when the 15th day in the 
# countdown is reached.
grad_days = graduation_countdown(days)
for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print(f"Days Left: {day}")

# It’s our lucky day! 
# The school president announces that graduation will now occur on the 3rd day
# left of the countdown. 
# Modify the for loop so that when the countdown day is 3, the generator will 
# close. 
# Insert the condition check and close() before the “Days Left” printout.

# We have three honors achievements to assign to students that are defined 
# within the summa(), magna(), and cum_laude() generator functions.
# Each honor is assigned based on a given GPA range listed below.
# Given a list of input GPAs, create a generator function called
# honors_generator that takes in 1 input argument named gpas that represents
# the list of GPAs from the variable gpas.
# The function should use yield from on each input GPA to determine the honors
# assignment.
def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()

honors = honors_generator(gpas)
for honor in honors:
  print(honor)