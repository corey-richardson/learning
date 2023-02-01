# Since doubly linked lists have a tail property, we don’t have to iterate 
# through the entire list to add to the tail like we did with a singly linked 
# list. The new method will mirror what we did in our .add_to_head() method:

# Start by checking to see if there is a current tail to the list
# If there is (meaning the list is not empty), then we want to reset the 
# pointers at the tail of the list:
#   Set the current tail’s next node to the new tail
#   Set the new tail’s previous node to the current tail
# Update the tail property to be the new tail
# Finally, if there isn’t a current head to the list (meaning the list was 
# empty):
#   Update the head property to be the new tail since that node will be 
#   both the head and tail

class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
    self.head_node = new_head
    if self.tail_node == None:
      self.tail_node = new_head

  # Define an .add_to_tail() method that takes self and new_value as parameters.
  # A new_tail Node that takes new_value as a parameter
  # A current_tail Node that’s set to the list’s tail
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node
    # If there is a current tail to the list:
    #   Set the current tail’s next node to new_tail
    #   Set new_tail‘s previous node to the current tail
    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
    # Outside your if statement, set the list’s tail to the new_tail.
    self.tail_node = new_tail
    # Lastly, if the list doesn’t have a head, set the list’s head to the 
    # new tail.
    if self.head_node == None:
      self.head_node = new_tail

