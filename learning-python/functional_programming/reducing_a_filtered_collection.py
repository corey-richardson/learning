from collections import namedtuple
from functools import reduce

# Prices are in USD
menu_item = namedtuple("menu_item", ["name", "dish_type", "price"])

jsp = menu_item("Jumbo Shrimp Platter", "Appetizer", 29.95)
lc = menu_item("Lobster Cake", "Appetizer", 30.95)
scb = menu_item("Sizzling Canadian Bacon", "Appetizer", 9.95)
ccc = menu_item("Codecademy Crab Cake", "Appetizer", 32.95)
cs = menu_item("Caeser Salad", "Salad", 14.95)
mgs = menu_item("Mixed Green Salad", "Salad", 10.95)
cp = menu_item("Codecademy Potatoes", "Side", 34.95)
mp = menu_item("Mashed Potatoes", "Side", 14.95)
a = menu_item("Asparagus", "Side", 15.95)
rs = menu_item("Ribeye Steak", "Entree", 75.95)
phs = menu_item("Porter House Steak", "Entree", 131.95)
grs = menu_item("Grilled Salmon", "Entree", 36.95)

menu = (jsp, lc, scb, ccc, cs, mgs, cp, mp, a, rs, phs, grs)
entree = 0
least_expensive = 0

# Given the extended menu for The Codecademy Steakhouse, using filter() 
# and reduce() find the most expensive dish that is an entree and assign 
# it to a variable called entree.
entree = reduce(lambda x,y: x if x.price > y.price else y, \
         filter(lambda x: x.dish_type == "Entree", menu))

print(entree)
# menu_item(name='Porter House Steak', dish_type='Entree', price=131.95)

# Using filter() and reduce(), find the least expensive dish that is either 
# a side or a salad and assign it to a variable called least_expensive. 
# Make sure to print out your answer!
least_expensive = \
    reduce(lambda x, y: x if x.price < y.price else y, \
    filter(lambda x: x.dish_type == "Side" or x.dish_type == "Salad", menu))
print(least_expensive)
# menu_item(name='Mixed Green Salad', dish_type='Salad', price=10.95)