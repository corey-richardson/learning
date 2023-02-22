
str_name = 'python powered patterned products'
str_word = 'patterned '

# This contains all of the functionality of a regular string, but it includes
# the string’s data inside of a property called data.
from collections import UserString

# Create a new class called SubtractString which inherits from UserString
class SubtractString (UserString):
  # In this class, overwrite the - operator to remove the string on the right
  # side of the operator from the string stored in the object.
  def __sub__(self, right):
    if right in self.data:
      self.data = self.data.replace(right, '')
      
# Create a new object from that class called subtract_string while passing 
# str_name in as the argument to the constructor.
# Next, use the - operator to subtract the substring str_word from 
# subtract_string.
subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)