dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}

# Using our dog food dictionary called dog_foods, create a variable called 
# dog_food_iterator that stores the value of calling iter() on our iterable 
# dog_foods.
dog_food_iterator = iter(dog_foods)

# Retrieve the first value of the dog_food_iterator using the built-in function 
# next() and set it to a variable called next_dog_food1.
next_dog_food1 = next(dog_food_iterator)
print(next_dog_food1)

# Retrieve the next two values of the dog_food_iterator using the __next__() 
# method and set them to the variables next_dog_food2 and next_dog_food3.
next_dog_food2 = dog_food_iterator.__next__()
next_dog_food3 = dog_food_iterator.__next__()
print(next_dog_food2)
print(next_dog_food3)

# What happens when we call next() or .__next__() after the last value of an 
# iterator object has been evaluated?
# next(dog_food_iterator)

# Traceback (most recent call last):
#   File "script.py", line 20, in <module>
#     next(dog_food_iterator)
# StopIteration