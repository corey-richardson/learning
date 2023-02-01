# Lambda functions are crucial in functional programming as they allow the 
# production of neat and concise functions that require other functions as 
# an argument.

# A lambda function is a short anonymous function that can accept several 
# parameters but only returns one value. Lambdas can be stored as a variable 
# or defined inline in the accepting function.


# Writing the function without lambdas, we have:
# ppsm: price per square meter
# dim: dimensions tuple

# def rect(b, h):
#   return b * h
# def tri(b, h):
#   return 0.5 * (b * h)
# def total_cost(ppsm, dim, area):
#   return ppsm * area(dim[0], dim[1])
# print(total_cost(3, (5, 5), rect)) # Rectangular sheet costing 75 units
# print(total_cost(4, (6, 7), tri)) # Rectangular sheet costing 84 units

## To make the code shorter, we can replace the rect(b,h) and the tri(b,h) 
# functions with lambdas like so:

# def total_cost(ppsm, dim, area):
#   return ppsm * area(dim[0], dim[1])
# print(total_cost(3, (5, 5), lambda b, h: b*h)) # Rectangular sheet costing 
# 75 units
# print(total_cost(4, (6, 7), lambda b, h: 0. 5 * b*h)) # Rectangular sheet 
# costing 84 units


# Lambda functions can be stored in a variable like so:
# rect = lambda x, y: x * y
# tri = lambda x, y: 0.5 * x * y

""" 
def squared(x):
  return x * x

def cubed(x):
  return x*x*x
"""

# Complete the odd_or_even() function provided. The body of the function will 
# return even_function(n) if n is even and return odd_function(n) if n is odd.
def odd_or_even(n, even_function, odd_function):
  if n % 2 == 0:
    return even_function(n)
  else: 
    return odd_function(n)

# Convert the functions squared(x) and cubed(x) into lambdas stored in 
# variables called square and cube respectively.
square = lambda x: x*x
cube = lambda x: x*x*x

# For this checkpoint, odd numbers are to be squared and even numbers are 
# to be cubed! Create a variable called test and set it to odd_or_even() 
# with n being 5 and pass in square and cube in the appropriate locations.
test = odd_or_even(5, cube, square)
print(test)