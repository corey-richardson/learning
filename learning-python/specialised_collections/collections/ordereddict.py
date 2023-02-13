from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# The OrderedDict container allows us to access values using keys, but it also 
# preserves the order of the elements inside of it.
# The order of the data is preserved when adding it to the OrderedDict.
# Data can be accessed using keys like a normal dictionary.
# The order can be retrieved by converting it to a list then accessing by index.

# # Move an item to the end of the OrderedDict
# orders.move_to_end('order_4829')
# # Pop the last item in the dictionary
# last_order = orders.popitem()

# Import the OrderedDict class and create a new object from that class called 
# orders.
from collections import OrderedDict
# Use the constructor to automatically convert the order_data into an 
# OrderedDict.
orders = OrderedDict(order_data)
# Create two new lists called to_move and to_remove.
to_move = []
to_remove = []
# Iterate through each item in orders and check what the status is. 
# If the status is 'returned' then add the key (order number string) to the 
# to_move list. Otherwise, if the status is 'canceled' then add it to the 
# to_remove list.
for key, value in orders.items():
  if value == 'returned':
    to_move.append(key)
  elif value == 'canceled':
    to_remove.append(key)
# For every item in the to_remove list, .pop() the element from orders.
for item in to_remove:
  orders.pop(item)
# Now that all of the canceled orders have been removed, use another loop to 
# push back any of the 'returned' orders from to_move to the end of orders. 
# This will be similar to the last step, but this time we are using the 
# .move_to_end() method.
for item in to_move:
  orders.move_to_end(item)

print(orders)