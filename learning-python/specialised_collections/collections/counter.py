# One of the most common tasks we might have to do in a program is to count 
# instances of an element in a collection. Below, we will examine a Python 
# list and look at one particular way we count elements, and then see how 
# the collections module allows us to improve upon our implementation using
# the Counter collection.

## WITHOUT COUNTER
# counted_items = {}
# for item in clothes_list:
#    if item not in counted_items:
#        counted_items[item] = 1
#    else:
#        counted_items[item] += 1
# print(counted_items)

## This would output (in no particular order):
# {'skirt': 8, 
#  'hoodie': 7, 
#  'dress': 5, 
#  'blouse': 6, 
#  'jeans': 8, 
#  'shoes': 6, 
#  'boots': 5, 
#  'jacket': 3, 
#  't-shirt': 2}

## WITH COUNTER
# from collections import Counter
# counted_items = Counter(clothes_list)
# print(counted_items)

## Would Output:
# Counter({'skirt': 8, 
#          'jeans': 8, 
#          'hoodie': 7, 
#          'blouse': 6, 
#          'shoes': 6, 
#          'dress': 5, 
#          'boots': 5, 
#          'jacket': 3, 
#          't-shirt': 2})


opening_inventory = [
    'shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 
    'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 
    'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 
    'dress', 'jeans', 'dress', 'blouse']

closing_inventory = [
    'shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 
    'dress', 'dress', 'jeans', 'dress', 'blouse']

# First, let’s define a function called find_amount_sold. 
# Our function will need three parameters: opening, closing, and item. 
# Also, don’t forget to import the Counter class as we will be using it 
# throughout the checkpoints.
from collections import Counter
def find_amount_sold(opening, closing, item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)
  # Next, we’ll have to subtract the closing counted data from the opening 
  # counted data in order to get the amount sold for every item. 
  # Luckily, the Counter container has a method that allows us to accomplish 
  # this really easily.
  # Call the .subtract() method on opening_count and pass in closing_count as 
  # the first argument.
  opening_count.subtract(closing_count)
  # Using the parameter item, access the item’s inventory from the 
  # opening_count Counter object and return it.
  return opening_count[item]

# Test out your function by calling it with opening_inventory as the first 
# argument, closing_inventory as the second argument, and t-shirt as the 
# third argument.
tshirts_sold = find_amount_sold(
  opening_inventory,
  closing_inventory,
  "t-shirt"
)
print(tshirts_sold) # 3