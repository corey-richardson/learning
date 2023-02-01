# In this exercise, we will review the map(), filter(), and reduce(), 
# higher-order functions provided by Python.

# https://www.codecademy.com/courses/learn-intermediate-python-3/articles/built-in-higher-order-functions-in-python

nums = \
(16, 2, 19, 22, 10, 23, 16, 2, 27, 29, 19, 26, 12, 20, 16, 29, 6, 2, 12, 20)

# Use filter() to remove odd numbers from tuple nums.
filtered_numbers = filter(lambda x: x%2==0, nums)
print(tuple(filtered_numbers))
# (16, 2, 22, 10, 16, 2, 26, 12, 20, 16, 6, 2, 12, 20)

# Using map() multiply all of the elements of nums by 3.
mapped_numbers = map(lambda x: x*3, nums)
print(tuple(mapped_numbers))
# (48, 6, 57, 66, 30, 69, 48, 6, 81, 87, 57, 78, 36, 60, 48, 87, 18, 6, 36, 60)

# Find the sum of all the elements in the tuple nums using the reduce() 
# function.
from functools import reduce
sum = reduce(lambda x,y: x+y, nums)
print(sum)
# 328

# Output:
# (16, 2, 22, 10, 16, 2, 26, 12, 20, 16, 6, 2, 12, 20)
# (48, 6, 57, 66, 30, 69, 48, 6, 81, 87, 57, 78, 36, 60, 48, 87, 18, 6, 36, 60)
# 328