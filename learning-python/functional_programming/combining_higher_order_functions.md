# Combining all Three Higher-Order Functions

Now that you’ve learned how to combine any two functions, let’s see how (and why) we can combine all three! A reason for doing this would be when you need to “filter” a collection before you “map” it (or “map” then “filter”) and then “reduce” it to a single number. To illustrate this in practice, let’s revisit the inventory problem from earlier, but this time we are only interested in the total sum of prices of items that sold for less than a certain value.

In this Python exercise, we are given the record of items represented by a dictionary. We are interested in the total sum of prices of items that sold for less than £150. We do this by:

- First “map” the items their individual total cost ((number of units sold) * (price per unit)).
- Then eliminate (“filter” out) all items that cost more than £150.
- Then “reduce” the individual costs to a single number that represents the total cost of the items.

We can do this with the following code:

```py
from functools import reduce
 
# Dictionary entry: {"name: (number_or_units_sold, price_per_unit_GBP)}
 
costs = {"shirt": (4, 13.00), "shoes":(2, 80.00), "pants":(3, 100.00), "socks":(5, 5.00), "ties":(3, 14.00), "watch":(1, 145.00)}
 
k = reduce(lambda x, y: x + y, filter(lambda r: r <= 150.00, map(lambda q: costs[q][0] * costs[q][1], costs)))
 
print(k) # Output will be a total cost of: 264.0 GBP
```

The focus of the code is:

```py
k = reduce(lambda x, y: x + y, filter(lambda r: r <= 150.00, map(lambda q: costs[q][0] * costs[q][1], costs)))
```
This first computes the total cost of each item using map():

```py
map(lambda q: costs[q][0]*costs[q][1], costs)
```

Then filter() is used to eliminate all items that cost more than £150:

```py
filter(lambda r: r <= 150.00, map(lambda q: costs[q][0] * costs[q][1], costs))
```

Then reduce() is used to compute the total sum:
```py
reduce(lambda x, y: x + y, filter(lambda r: r <= 150.00, map(lambda q: costs[q][0] * costs[q][1], costs)))
```
