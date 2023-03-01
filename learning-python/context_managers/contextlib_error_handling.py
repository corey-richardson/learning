from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  # Add an except clause to the poem_files context manager so that it 
  # catches an AttributeError exception, saves it as a variable called e.
  except AttributeError as e:
    # Print e inside of the except block.
    print(e)
  finally:
    print('Closing File')
    open_poem_file.close()

with poem_files('poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.sign('Buzz is big city. big city is buzz.')

