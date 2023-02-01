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

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

  # Define a .remove_head() method that only takes self as a parameter. 
  # Inside, create a removed_head variable and set it to the list’s head node.
  def remove_head(self):
    removed_head = self.head_node
    # Check if removed_head has no value.
    if removed_head == None:
      # If so, that means there’s nothing to remove, so return None to end the
      # method.
      return None
    # Outside of your if, set the list’s head to removed_head‘s next node.
    # If the list still has a head, set its previous node to None, since 
    # the head of the list shouldn’t have a previous node.
    self.head_node = removed_head.get_next_node()
    if self.head_node != None:
      self.head_node.set_prev_node(None)
    # Check if removed_head is equal to the list’s tail. If so, call the 
    # .remove_tail() method (we will create this in the next exercise).
    if removed_head == self.tail_node:
      self.remove_tail() # **(we will create this in the next exercise)**
    # Finally, return removed_head‘s value.
    return removed_head.get_value()
