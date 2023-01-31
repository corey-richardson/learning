# Define your Node class below:
# Let’s implement a linked list in Python. As you might recall, each linked list is a sequential chain of nodes. So before we start building out the LinkedList itself, we want to build up a Node class in Python that we can use to build our data containers.

class Node:
  # CONSTRUCTOR
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node

  # GETTERS
  def get_value(self):
    return self.value
  def get_next_node(self):
    return self.next_node

  # SETTERS
  def set_next_node(self, next_node):
    self.next_node = next_node
  
my_node = Node(44)
print( my_node.get_value() )