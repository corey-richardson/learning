# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Create your LinkedList class below:

# get the head node of the list (it’s like peeking at the first item in line)
# add a new node to the beginning of the list
# print out the list values in order
# remove a node that has a particular value

class LinkedList:
  def __init__(self, value=None):
    # set self.head_node equal to a new Node with value as its value
    self.head_node = Node(value)

  def get_head_node(self):
    # return the head node of the linked list
    return self.head_node