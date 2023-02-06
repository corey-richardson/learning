# If we desire to create our own custom iterator class, we must implement the iterator protocol, meaning we need to have a class that defines at minimum the __iter__() and __next__() methods.
# To make the FishInventory class iterable, we can simply define __iter__() and __next__() methods.

class FishInventory:
  def __init__(self, fishList):
      self.available_fish = fishList

fish_inventory_cls = FishInventory(["Bubbles", "Finley", "Moby"])

# Write your code below:
for feesh in fish_inventory_cls:
  print(feesh)

# Traceback (most recent call last):
#   File "script.py", line 11, in <module>
#     for feesh in fish_inventory_cls:
# TypeError: 'FishInventory' object is not iterable