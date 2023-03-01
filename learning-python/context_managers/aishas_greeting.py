# Iimport the contextlib modules @contextmanager decorator, and create a 
# decorated function named generic that takes in card type, sender’s name,
# and recipient arguments.
from contextlib import contextmanager
@contextmanager
def generic(card_type, senders_name, recipient):
  # A variable to store a call of the open() built-in function that opens up a 
  # generic card type based on the card type parameter in read mode. 
  # You can assume the store will receive either a birthday card request or 
  # a thank you card request.
  # A variable to store a call of the open() built-in function that creates 
  # (and opens) a new card named with the following pattern: 
  # < sender_name >_generic.txt.
  card_file = open(card_type, 'r')
  order = open(f"{senders_name}_generic.txt", "w")
  
  try:
    # Inside the generic() context manager use the try clause to yield a file 
    # so that it creates the following template custom card:
    order.write(f"Dear {recipient}, \n")
    order.write(card_file.read())
    order.write(f"\nSincerely, {senders_name} \n")
    yield order
  # close both files after usage
  finally:
    card_file.close()
    order.close()

# Aisha’s Greetings just got a customer ‘Mwenda’ who requested an order for a 
# generic Thank you card for her friend ‘Amanda’.
# Use a with statement to generate this order. Have the with statement confirm
# the card is created by printing 'Card Generated!'.
with generic("thankyou_card.txt", "Mwenda", "Amanda") as order1: 
  print('Card Generated! \n')
# Use a with statement to open and read the file you just created in the 
# last step.
with open("thankyou_card.txt", "r") as first_order:
 print(first_order.read())

# create a class called personalized.
class personalized:
  # write a __init__ method that takes the sender’s and receiver’s names and
  # saves them as attributes.
  def __init__(self, senders_name, recipient):
    self.file = open(f"{senders_name}_personalized.txt", 'w')
    self.senders_name = senders_name
    self.recipient = recipient
    
  # Make an __enter__ method that writes the receiver’s name to the opened file
  # and returns that file.
  def __enter__(self):
    self.file.write(f"Dear {self.recipient}, \n \n")
    return self.file
  
  # Create an __exit__ method that writes "Sincerely" followed by the sender’s
  # name on the open file and then closes the file!
  def __exit__(self, exc_type, exc_value, Traceback):
    self.file.write(f"\n \n Sincerely, \n {self.senders_name}")
    self.file.close()



with personalized("John", "Michael") as card:
  card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with generic("happy_bday.txt","Josiah","Remy" ) as card, personalized("Josiah","Esther") as card2:
  card2.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")
