# To make it iterable, we first define the __iter__() method. We can initialize 
# a class member within the __iter__() method called index that will help us 
# track the current position we’re in within the self.available_fish list.

# def __iter__(self):
#   self.index = 0
#   return self
# def __next__(self):
  # fish_status = self.available_fish[self.index] + " is available!"
  # self.index += 1
  # return fish_status

class CustomerCounter:
  # A custom class called CustomerCounter that counts the number of customers in 
  # the store. Make this class iterable by first defining the __iter__() method.
  def __iter__(self):
    self.count = 0
    return self
  # Next, define the __next__() method. Only 1 customer will enter at a time each
  # time this __next__() method is called.
  def __next__(self):
    if self.count >= 100:
      raise StopIteration
    else:
      self.count += 1
    return self.count

# Create a class instance customer_counter from the CustomerCounter class.
customer_counter = CustomerCounter()

# If we were to iterate through the customer_counter object using a for loop now, 
# we would get an infinite loop since our __next__() method has not raised a 
# StopIteration exception.
# Modify the __next__() method to raise a StopIteration exception when our customer
# count is greater than 100.

# Create a for loop to iterate through our CustomerCounter class object 
# customer_counter.
for customer in customer_counter:
  print(customer)