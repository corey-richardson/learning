# We’ve learned that we can create our own context managers using the 
# class-based method, but there’s an even simpler way of creating context 
# managers. We can use a built-in Python module called contextlib!
# The contextlib module allows for the creation of a context manager with the 
# use of a generator function (a function that uses yield instead of return) 
# and the contextlib decorator - @contextmanager. 
# Instead of creating a classand definining __enter__ and __exit__ methods, 
# we can use a simple function!

from contextlib import contextmanager

# Once we have successfully imported the module, we can automatically use the @contextmanager decorator to wrap a simple generator function

# @contextmanager
# def open_file_contextlib(file, mode):
#   opened_file = open(file, mode)
#  try:
#    yield opened_file
#  finally:
#    opened_file.close()

# We have written a generator function called open_file_contextlib with the 
# expectation that it will take in two arguments, a file and a mode.
# We then use the built-in open() function to open the file (that we received
# as an argument) and save it to a variable called opened_file.
# The function then will attempt (via a try statement) to yield the opened
# file and complete whatever code we pass when we use it in conjunction with
# the with statement. More on this in a bit!
# Lastly the resource (file) will be closed once all the code is done being 
# executed.

# with open_file_contextlib('file.txt', 'w') as opened_file:
#  opened_file.write('We just made a context manager using contexlib')

# ---

# Create a generator function called poem_files that has two parameters file 
# and mode. The function should do two things:
# - Print 'Opening File'
# - Open the file using open() with the file and mode parameters, and save the
#   result to a variable called open_poem_file.
# Don’t forget to decorate it with the @contextmanager decorator.
@contextmanager
def poem_files(file, mode):
  print("Opening File")
  open_poem_file = open(file, mode)
  # Next, we will have to create the try/finally structure. 
  # Inside of the function write the try clause, and inside of it use the
  # yield keyword to yield the open_poem_file variable.
  try:
    yield open_poem_file
  # Now, let’s finish the try/finally block by writing a finally clause that
  # does two things:
  #   Print 'Closing File'
  #   Call close() on the open_poem_file variable.
  finally:
    print("Closing File")
    open_poem_file.close()


with poem_files('poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.write('Rose is beautiful, Just like you.')

