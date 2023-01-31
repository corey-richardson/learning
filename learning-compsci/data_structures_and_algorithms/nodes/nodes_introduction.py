# Create the Node class below:
# Begin by creating a new class, Node. Add an .__init__() method in the Node
# class that takes a value and an optional link_node (default should be None). 
# These should be saved to the corresponding self properties (self.value and
# self.link_node).

class Node:
  def __init__(self, value, link_node = None):
    self.value = value
    self.link_node = link_node
