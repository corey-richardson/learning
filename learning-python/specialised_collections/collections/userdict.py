# The UserDict container wrapper lets us create our own version of a dictionary. 
# This class contains all of the functionality of a normal dict, except that 
# we can access the dictionary data through the data property.

data = {'order_4829': 
            {'type': 't-shirt', 'size': 'large', 
             'price': 9.99, 'order_status': 'processing'},
        'order_6184': 
            {'type': 'pants', 'size': 'medium', 
             'price': 14.99, 'order_status': 'complete'},
        'order_2905':
            {'type': 'shoes', 'size': 12, 
             'price': 22.50, 'order_status': 'complete'},
        'order_7378': 
            {'type': 'jacket', 'size': 'large', 
             'price': 24.99, 'order_status': 'processing'}}

# Import the UserDict class and create a new class which inherits from it called
# OrderProcessingDict.
from collections import UserDict

class OrderProcessingDict (UserDict):
  # The .clean_orders() method should search for any keys called ‘order_status’
  # and if value is equal to 'complete', remove the entire order from the
  # dictionary.
  def clean_orders(self):
    to_delete = []
    for key, val in self.data.items():
      if val['order_status'] == 'complete':
        to_delete.append(key)
    for item in to_delete:
      del self.data[item]

# Create an instance of it called process_dict while passing data into the 
# constructor. 
# Afterwards, call the .clean_orders() method to automatically clean the
# orders inside.
process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
print(process_dict)