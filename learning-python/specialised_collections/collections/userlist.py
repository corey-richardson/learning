# Not only can we create our own version of a dictionary, the UserList wrapper container lets us create our own list as well! This class contains all of the functionality of a regular list, but it also has a property called data which allows us to access the list contents directly.

data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

from collections import UserList
# Create a new class called ListSorter which inherits from the UserList class.
# Inside of this class, overwrite the .append() method to sort the list after appending the value to it.
class ListSorter (UserList):
  def append(self, to_append):
    self.data.append(to_append)
    self.sort()

# Create an object called sorted_list and pass data into the ListSorter constructor. 
# Afterwards, append the value 2 to the new object and print out the results.
sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)
