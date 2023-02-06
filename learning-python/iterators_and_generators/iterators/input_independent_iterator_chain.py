# An input-dependent iterator will terminate based on the length of one or more
# input values. They are great for working with and modifying existing iterators.
# chain() takes in one or more iterables and combine them into a single iterator.

# import itertools
# odd = [5, 7, 9]
# even = {6, 8, 10}
# all_numbers = itertools.chain(odd, even)
# for number in all_numbers:
#   print(number)

# Imports the itertools module.
# Sets all_numbers to the iterator returned by the itertool chain().
# Uses the list iterable odd and the set iterable even as the arguments to chain().
# Implements a for loop using the iterator in all_numbers
# Prints the results, which will be:
# 5 7 9 8 10 6
# Python sets are not ordered so the last 3 numbers in this example’s output will 
# not always be in the initialized order.

import itertools

great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Obtain a master list of SKU numbers for all bags of dog food, regardless of 
# brand.
# Use the chain() itertool set to a variable named all_skus_iterator to combine
# the SKU lists.
all_skus_iterator = \
itertools.chain(great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)

for sku in all_skus_iterator:
  print(sku)
