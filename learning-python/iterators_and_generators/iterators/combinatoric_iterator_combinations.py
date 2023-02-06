# To show how it’s used, suppose we have a list of even numbers and we want all
# possible combinations of 2 even numbers:

# import itertools
# even = [2, 4, 6]
# even_combinations = list(itertools.combinations(even, 2))
# print(even_combinations)

# Import the module itertools.
# Create an iterator using combinations() with the list of even numbers as the 
# first argument and 2 as the second argument.
# Set even_combinations equal to a list of the elements in the iterator returned
# from combinations().
# Print even_combinations. The resulting list of 2 member tuples are the 
# combinations of all 3 members of even:
# [(2, 4), (2, 6), (4, 6)]

# A combinatoric iterator will perform a set of statistical or mathematical 
# operations on an input iterable.

import itertools

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# We have another shelving unit to display by the register that can only hold
# 3 collars. We have a list of collars of varying colors and sizes.
# We want to know how many different combinations exist to display a set of 3
# collars. Use the combinations() itertool to do this. 
# Set the returned iterator to a variable named collar_combo_iterator.

collar_combo_iterator = itertools.combinations(collars, 3)
for combi in collar_combo_iterator:
  print(combi)
