# An infinite iterator will repeat an infinite number of times with no endpoint 
# and no StopIteration exception raised. Infinite iterators are useful when we 
# have unbounded streams of data to process.

# count(start,[step])
# The first argument of count() is the value where we start counting from. 
# The second argument is an optional step that will return current 
# value + step.

# import itertools
# for i in itertools.count(start=0, step=2):
#   print(i)
#   if i >= 20:
#     break
# OUTPUT:
# 0 2 4 6 8 10 12 14 16 18 20

# ---

# # We have several 13.5lb bags of dog food to display. Our single shelving
# unit however can only hold a maximum of 1,000lbs. Let’s figure out how many
# bags of food we can display!

# First, import the itertools module at the top line of the code editor.
import itertools

max_capacity = 1000
num_bags = 0

# We start with the first 13.5lb bag, which means our start value is 13.5, and
# each subsequent bag after that is 13.5lbs.
for i in itertools.count(13.5, 13.5):
  # Provide a stop condition using max_capacity to terminate the loop
  if i >= max_capacity:
    break
  num_bags += 1
print(num_bags)
