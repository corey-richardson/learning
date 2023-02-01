# The dictionary provided represents the number of a given fruit sold over 
# three days - a dictionary entry is:
# fruit_name:(amount sold on day 1, amount sold on day 2, amount sold on day 3)
# Using map() and reduce(), find the total number of fruits sold. 
# Store this answer in a variable called total_fruits. 

# The parameters and return value in the reduce() function’s lambda must all 
# be of the same type. To do this, we must sum up the values in the dictionary 
# entries to produce one number for each entry: the total number of each fruit 
# sold. We can do this using map(). Recall that we did this in the example 
# provided earlier like so:
# map(lambda q: costs[q][0]*costs[q][1], costs)
# In this case, the map() function must add the three values for each entry 
# in fruits.
# reduce() is used to add up each total.

from functools import reduce

fruits = {"Grape":(4, 6, 2), "Lemon":(7, 3, 1), "Orange":(5, 8, 1), "Apple":(2, 8, 10), "Watermelon":(0, 9, 6)}


# Code for Checkpoint 1 goes here.
total_fruits = \
reduce(lambda x,y: x+y, \
map(lambda n: fruits[n][0] + fruits[n][1] + fruits[n][2], fruits))

print(total_fruits)
