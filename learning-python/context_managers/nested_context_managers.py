from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()


@contextmanager
def card_files(file, mode):
  print('Opening File')
  open_card_file = open(file, mode)
  try:
    yield open_card_file
  finally:
    print('Closing File')
    open_card_file.close()

# Write a nested context manager that uses the poem_files context manager to 
# open poem.txt in read mode and saves it to a variable called poem
# Nested inside, use the card_files context manager to open the card.txt file 
# in write mode and saves it to a variable called card.
# Print poem and card to confirm we can access both files.
with poem_files("poem.txt", "r") as poem:
  with card_files("card.txt", "w") as card:
    print(poem)
    print(card)
    # Inside of our nested context managers, and under our print statements,
    # write to card.txt the contents of poem.txt.
    card.write(poem.read())