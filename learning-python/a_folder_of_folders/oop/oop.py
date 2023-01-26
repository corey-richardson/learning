comment = '''
Programming paradigms
- Object orietation
- Procedural
- Functional

- OOP
Encapsulation
Abstraction
Inheritance
Polymorphism
'''

class Employee:
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id+=1
  def say_id(self):
    print("My ID is %i" % self.id)

e1 = Employee()
e1.say_id()

e2 = Employee()
e2.say_id()

# class ParentClass:
#   #class methods/properties...
 
# class ChildClass(ParentClass):
#   #class methods/properties...

# class Animal: 
#   def eat(self): 
#     print("Nom Nom Nom...eating food!")
    
# class Dog(Animal):
#   def bark(self):
#     print('Bark!')
 
# class Cat(Animal):
#   def meow(self):
#     print('Meow!')
    
# fluffy = Dog()
# zoomie = Cat()
 
# fluffy.eat() # Nom Nom Nom...eating food!
# zoomie.eat() # Nom Nom Nom...eating food!

class Admin(Employee):
    pass

e3 = Admin()
e3.say_id()

# OVERRIDING METHODS

class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self): # defined make_noise to output "grrr"
    print("{} says, Grrrr".format(self.name))
 
pet1 = Animal("Rex")
pet1.make_noise() # Rex says, Grrrr

class Cat(Animal):
 
  def make_noise(self): # cats dont say grrr, they say meow
    print("{} says, Meow!".format(self.name))
 
pet2 = Cat("Maisy")
pet2.make_noise() # Maisy says, Meow!

# dunder