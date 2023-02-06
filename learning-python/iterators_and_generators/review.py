# Create a list iterable that contains tuples of (cat_toy, price). 
# The list should be called cat_toys.
# Using iter(), create an iterator called cat_toy_iterator that retrieves the 
# iterator for cat_toys.
# Using iter(), create an iterator called cat_toy_iterator that retrieves the 
# iterator for cat_toys.
# A customer enters and only has $15 to spend on exactly 2 cat toys. 
# They want to know how many combinations of the available toys they can afford,
# while only getting 2 of them total.
# First, import itertools at the top of the module.
# Next, above the commented out for loop, create a combinations() iterator called
# toy_combos to retrieve all combinations of 2 total toys from the cat_toys list.
# Uncomment all lines of the for loop.
# Each iteration of the for loop gives a tuple that is within toy_combos. 
# The variable toy1 represents index 0 of the tuple (the toy name) and cost_of_toy1
# represents index 1 of the tuple (the toy cost). We repeat this to store the toy 
# name and price of toy 2 via variables toy2 and cost_of_toy2.
# After the final line within the for loop, check if the price of cost_of_toy1 and
# cost_of_toy2 is less than or equal to max_money which is the max $15 the customer
# has to spend. 
# If it is, add the tuple to the options list.
# Print the final options list to see what toy combinations the customer can 
# buy with $15.

cat_toy = ["laser","fountain","scratcher","catnip"]
price =   [1.99,    5.99,      10.99,      15.99  ]
cat_toys = list( zip( cat_toy, price ) )

max_money = 15
options = []

cat_toy_iterator = iter(cat_toys)

print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))

import itertools
toy_combos = itertools.combinations(cat_toys, 2)

for combo in toy_combos:
   toy1 = combo[0]
   cost_of_toy1 = toy1[1]
   toy2 = combo[1]
   cost_of_toy2 = toy2[1]

   if cost_of_toy1 + cost_of_toy2 <= max_money:
     options.append(combo)
  
print(options)