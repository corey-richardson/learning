# open_file = open('file_name.txt', 'r')
# print(open_file.read())

# Take a look at the code in the text editor. Notice that the file ('file_name.txt') was opened but never closed. This is bad practice and could lead to errors down the road.
# Update this script by:
# - Putting the code that opens the file inside a try block
# - Closing open_file in a finally block using .close()

try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()

# Now rewrite this script in with statement form using open_file as the target variable. 
# Use the "r" mode for read permissions.

with open('file_name.txt', 'r') as open_file:
  print(open_file.read())