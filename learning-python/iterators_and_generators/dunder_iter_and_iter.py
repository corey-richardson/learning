# the for loop has to do is to convert our dictionary (the iterable) of dog_foods
# to an iterator object

# dog_food_iterator = iter(dog_foods)
# print(dog_food_iterator)
# <dict_keyiterator object at 0x....> 
# Calling dog_foods.__iter__() will retrieve the same iterator object as calling 
# iter(dog_foods)

sku_list = [7046538, 8289407, 9056375, 2308597]

# Suppose we have a list of SKUs (stock-keeping units) for products in our pet 
# shop. Let’s examine the internal methods of the iterable sku_list.
# Use dir() on sku_list and print out the result. Can you spot __iter__ in the
# list of methods that are printed?
print(dir(sku_list))

# Let’s access the internal __iter__() method from sku_list to create our 
# iterator object.
# Create a variable called sku_iterator_object_one that is equal to calling 
# .__iter__() on sku_list.
sku_iterator_object_one = sku_list.__iter__()
print(sku_iterator_object_one)

# Create a variable called sku_iterator_object_two that is equal to calling 
# iter() on sku_list.
sku_iterator_object_two = iter(sku_list)
print(sku_iterator_object_two)