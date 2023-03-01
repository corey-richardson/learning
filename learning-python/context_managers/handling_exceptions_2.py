# An exception that occurs in a context manager can be handled in two ways:
# If we want to throw an error when an error occurs, we can either:
#   Return False after the .close() method
#   Do nothing
# If we want to suppress the error, we can:
#   Return True after the .close() method

class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print(' \n --  Opening poem file -- \n')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback, '\n')
    # Inside of the __exit__ method, write a conditional using the isinstance() function to check if the exception is an AttributeError. If it is, close the file and return True!
    if isinstance(exc_value, AttributeError):
      self.opened_poem_file.close()
      return True
    

with PoemFiles('poem.txt', 'r') as file:
  print("---- Exception data below ---- \n ")
  print(file.uppercasewords())

with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print(" \n ---- Exception data below ---- \n ")

