clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# we use a CapWords convention when defining our namedtuple. 
# This is because namedtuple actually returns a subclass and thus falls under 
# the conventions we use for classes.

# Import the container and create a namedtuple subclass called ClothingItem 
# with a typename of 'ClothingItem' and the field_name consisting of: 
# 'type', 'color', 'size', and 'price' in that specific order.
from collections import namedtuple
ClothingItem = namedtuple("ClothingItem", ["type","color","size","price"])

# Create a new object from the subclass ClothingItem called new_coat.
# The new_coat should have a type of 'coat', a color of 'black', a size of 
# 'small', and a price of 14.99.
new_coat = ClothingItem("coat","black","small",14.99)

# Now that the new_coat object has been created, access the price of this 
# namedtuple object and store it in a variable called coat_cost.
coat_cost = new_coat.price
print(f"Coat Cost: {coat_cost}")

# create a new empty list called updated_clothes_data and then for every piece
# of clothes data in the list of tuples, append a new ClothingItem object to 
# updated_clothes_data while passing the data from the tuple into the new 
# ClothingItem object.
updated_clothes_data = list()
for item_info in clothes:
  print(list(item_info))
  updated_clothes_data.append
  (
    ClothingItem (item_info[0], item_info[1], item_info[2], item_info[3])
  )
print(updated_clothes_data)