class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n ')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  # Create an __exit__ method, and add the 4 necessary arguments: self, exc_type, exc_value, traceback. 
  # Have the method use 3 different print statements to print each exception argument.
  def __exit__ (self, exc_type, exc_value, traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    self.opened_poem_file.close()

# First
# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ----")
#   print(file.uppercasewords())

# -- Starting up a poem context manager -- 
# Opening poem file
# ---- Exception data below ----
# <class 'AttributeError'>
# '_io.TextIOWrapper' object has no attribute 'uppercasewords'
# <traceback object at 0x7f94739fb7c8>
# Traceback (most recent call last):
#   File "script.py", line 24, in <module>
#     print(file.uppercasewords())
# AttributeError: '_io.TextIOWrapper' object has no attribute 'uppercasewords'

# Second
# with PoemFiles('poem.txt', 'r') as file2:
#   print(file2.read())
#   print("---- Exception data below ----")

# -- Starting up a poem context manager -- 
# Opening poem file
# She gives her cloud a shake,
# And laughs until her belly aches.
# The only other sound's the break,
# Of distant waves and birds awake.
# ---- Exception data below ----
# None
# None
# None

