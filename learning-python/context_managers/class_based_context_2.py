# Create a class called PoemFiles and give it a __init__ method that defines 
# a self, poem_file, and mode parameter.
# Inside the method, print 'Starting up a poem context manager'
# Inside of the __init_ method and under the print statement, assign two 
# properties to the class:
# file that is equal to the poem_file parameter
# mode that is equal to the mode parameter
class PoemFiles:
  def __init__ (self, poem_file, mode):
    print("Starting up a poem context manager")
    self.file = poem_file
    self.mode = mode

  # Create an __enter__ method. Have the method print 'Opening poem file'.
  # Inside __enter__ method give the class a new property called opened_poem_file
  # and assign it to a call of the open() function that takes two arguments:
  # self.file: our classes file property
  # self.mode: our classes mode property
  # Lastly, return the opened_poem_file property!
  def __enter__ (self):
    print("Opening poem file")
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  # Write a __exit__ method that defines a self parameter and a *exc parameter. 
  # Make the method print 'Closing poem file'.
  # In the __exit__ method, under the print statement, call the .close() built-in
  # function on the opened_poem_file property of the class.
  def __exit__ (self, *exc):
    print("Closing poem file")
    self.opened_poem_file.close()

with PoemFiles('poem.txt', 'w') as open_poem_file:
   open_poem_file.write('Hope is the thing with feathers')