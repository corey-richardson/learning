# In Python, wrappers are modifications to functions or classes which change 
# the behavior in some way. 
# They are called wrappers because they “wrap” around the existing code 
# to modify it. 
# This is most commonly used with function wrapping, but we can also wrap 
# classes.

# In the case of containers, the collections class has three different wrapper
# classes set up for us to modify! Because of this, we can refer to them as 
# wrapper containers. 
# The advanced containers which we have already been looking at are variations 
# of the standard built-in containers, so using wrapper containers allows us 
# to create our own versions as well.
# The three wrapper containers we will be looking at are:
# UserDict
# UserList
# UserString

# First, we need a class to wrap around.
class Customer:
    
  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number

# Next, we create a wrapper class which stores an object of the class we are
# wrapping around. 
# It also includes some additional functionality.
class CustomerWrap(Customer):
    
  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)
 
  def display_customer_info(self):
    print('Name: ' + self.customer.name)
    print('Age: ' + str(self.customer.age))
    print('Address: ' + self.customer.address)
    print('Phone Number: ' + self.customer.phone_number)

# Finally, we can create an object from the wrapper class to access the new 
# functionality and the wrapped class contained inside.
customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()