# Reducing a Filtered Collection

In this exercise, we will explore how to use `reduce()` and `filter()` together. Let’s consider the following example. We have a tuple representing the menu items for a fictitious restaurant: The Codecademy Steakhouse. We wish to find the least expensive appetizer on the menu. We can express this process by the sentence: "filter the menu for appetizers and return the least expensive one." Let’s do this imperatively first.

```py
from collections import namedtuple
from functools import reduce
 
# Prices are in USD
menu_item = namedtuple("menu_item", ["name", "dish_type", "price"])
 
jsp = menu_item("Jumbo Shrimp Platter", "Appetizer", 29.95)
lc = menu_item("Lobster Cake", "Appetizer", 30.95)
scb = menu_item("Sizzling Canadian Bacon", "Appetizer", 9.95)
ccc = menu_item("Codecademy Crab Cake", "Appetizer", 32.95)
cs = menu_item("Caeser Salad", "Salad", 14.95)
mgs = menu_item("Mixed Green Salad", "Salad", 11.95)
cp = menu_item("Codecademy Potatoes", "Side", 34.95)
mp = menu_item("Mashed Potatoes", "Side", 14.95)
rs = menu_item("Ribeye Steak", "Entree", 75.95)
phs = menu_item("Porter House Steak", "Entree", 131.95)
 
menu = (jsp, lc, scb, ccc, cs, mgs, cp, mp, rs, phs)
```

```py
# Imperative solution:
# apps only contains items with dish_type == "Appetizer"
apps = [i for i in menu if i.dish_type == "Appetizer"] 
cheapest_app = app[0] 
for i in apps:
  if i.price < cheapest_app.price:
    cheapest_app = i
 
print(cheapest_app) 
# Output will be: menu_item("Sizzling Canadian Bacon", "Appetizer", 9.95)
```

We can eliminate the for loop and do this declaratively by using filter() and reduce() like this:

```py
cheapest_app = reduce(lambda x, y: x if x.price < y.price else y, \
    filter(lambda x: x.dish_type == "Appetizer", menu))
 
print(cheapest_app)
 # Output will be: menu_item("Sizzling Canadian Bacon", "Appetizer", 9.95)
```

In the reduce() function, the lambda `lambda x, y: x if x.price < y.price else y`returns the cheaper of the two `menu_items` compared by their price.

The `filter()` function returns an iterable with all `menu_items` that have “Appetizer” as dish_type. This iterable is then passed into `reduce()` to be processed by its lambda function. Combining these two functions converts the imperative code into a one-line solution!