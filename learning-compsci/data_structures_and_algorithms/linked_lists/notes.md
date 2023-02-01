# Linked Lists

A linked list is a dynamic data structure, which means that the size of the list can change at run time. <br> You can imagine a linked list as a chain where each link is connected to the next one to form a sequence with a start and an end.

Each element in a linked list is called a node. Each node stores:
- The data relating to the element
- A pointer to the next node

There is also a separate pointer that indicates the first element in the list (the head of the list). This has a null value when the list is empty. The next node pointer of the last element in the list always points to a null value to mark the end of the list.

![Diagram: A linked list with four nodes (each containing a value)](https://isaaccomputerscience.org/api/v3.4.1/api/images/content/computer_science/data_structures_and_algorithms/data_structures/figures/isaac_cs_dsa_data_struct_linked_list_pointer.png)

An additional pointer can be used to indicate the last element of the list (the tail of the list). This is useful when implementing a queue using a linked list so that the end of the list can be accessed without needing to traverse the list.

---

## Implementing a Linked List

A class is defined to represent a node. The node contains:
- a variable to store the the data value of the element
- a pointer to the next node

A second class is defined to represent the list. This needs a single attribute:
- a pointer to the head of the list

#### Psuedocode
```
CLASS Node 
    PRIVATE data: String
    PRIVATE next: Node

    // Constructor method
    PUBLIC PROCEDURE Node(given_data) 
        data = given_data
        next = Null
    ENDPROCEDURE
ENDCLASS


CLASS LinkedList
    PRIVATE head: Node

    // Constructor method
    PUBLIC PROCEDURE LinkedList() 
        head = Null
    ENDPROCEDURE
ENDCLASS 


// Instantiate an empty linked list object
my_list = NEW LinkedList()
```

#### Python
```py
class Node():
    def __init__(self, given_data):
        """Constructor method"""
        self.data = given_data
        self.next = None


class LinkedList():
    def __init__(self):
        """Constructor method"""
        self.head = None


# Instantiate an empty linked list object
my_list = LinkedList()
```

#### C#
```cs
class Node
{
    private string data;
    private Node next;

    // Constructor method
    public Node(string givenData)
    {
        data = givenData;
    }
}


class LinkedList
{
    private Node head;
}


// Instantiate an empty linked list object
LinkedList myList = new LinkedList();
```

---

## Traversing a Linked List

Traversing means to work your way systematically through the list. You may need to do this to find an element in the list or if you wanted to display the contents of the list.

To traverse a linked list you need to start from the first node (referenced by head) and follow each next link until you reach the last node (whose next pointer will be Null).

If head is equal to Null then the list is empty.

#### Psuedocode
```
CLASS Node
    
    ....
    PUBLIC FUNCTION get_data()
        return data
    ENDFUNCTION
    
    PUBLIC FUNCTION get_next()
        return next
    ENDFUNCTION  
    
    PUBLIC PROCEDURE set_next(new_next)
        next = new_next
    ENDPROCEDURE

ENDCLASS


CLASS LinkedList   
   
   ....
    PROCEDURE traverse()
        // Set the current node as the head
        current = head

        // Repeat until there are no more linked nodes
        WHILE current != Null
            PRINT(current.get_data())
 	        current = current.get_next()
        ENDWHILE
    ENDPROCEDURE
   
ENDCLASS 
```

#### Python
```py
class Node():

    ....
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList():
    
    ....
    def traverse(self):        
        # Set the current node as the head
        current = self.head

        # Repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current = current.get_next()
```

#### C#
```cs
class Node
{
    ....
    public string GetData()
    {
        return data;
    }

    public Node GetNext()
    {
        return next;
    }

    public void SetNext(Node newNext)
    {
        next = newNext;
    }
}


class LinkedList
{
    ....
    public void Traverse() 
    {
        // Set the current node as the head
        Node current = head;

        // Repeat until there are no more linked nodes
        while (current != null) {
            Console.WriteLine(current.GetData());
            current = current.GetNext();
        }
    }
}
```

---

## Adding a New Node

### Unordered List

To add a node to an unordered linked list, you can add the new node to the start or to the end of the list. To add it to the end, you must traverse the list to find the last element. Thus, it is more efficient to add the new node to the front of the list.

To add a new node to the front of a list, you must:
- create the new node
- set the next pointer of the new node to the value of the head pointer (of the linked list)
- set the head pointer (of the linked list) to point to the new node

### Ordered List

If the list is ordered, the new element must be inserted into the correct position. The following steps define the process for inserting a new element into a list where the elements are ordered in ascending order, from lowest to highest value. These steps work for both numerical order (from lowest to highest number), or alphabetical order (from A-Z) based on the character code.

- create a new node
- set the current node as the head of the list
- traverse the list to find the correct position for the new node:
    - continue while the next pointer of the current node is not Null
    - continue while the data of the next node from the current node is less than the data of the new node
    - set the current node to be the next node
- once the correct position has been found:
    - set the next pointer of the new node to be the next pointer of the current node
    - set the next pointer of the current node to be the new node

Notice that you don't need to move any other nodes to put the new node in the correct place. Because a linked list uses pointers, all you need to do is to change the pointers to maintain the correct order.

#### Python
```py
class LinkedList():
    
    ....
            
    def insert_in_order(self, data):
        """Insert a node into the correct position in an ordered list"""

        # Create a new node
        new_node = Node(data)

        # Start at the head of the list
        current = self.head
        
        # Check if there are no nodes in the list
        if current is None:
            self.head = new_node

        # Check if the new node data is before the head data
        elif new_node.get_data() < current.get_data():
            # Set the new node as the head of the list
            new_node.set_next(self.head)
            self.head = new_node

        # Otherwise find where the new node should be positioned
        else:
            # Repeat until the point of insertion is found
            while (current.get_next() is not None
                  and current.get_next().get_data() < new_node.get_data()):
                # Get the next node
                current = current.get_next()

            # Update the pointers of the new and current nodes
            new_node.set_next(current.get_next())
            current.set_next(new_node)
```

#### C#
```cs
class LinkedList
{
    ....

    public void InsertInOrder(string data)
    {
        // Create a new node
        Node newNode = new Node(data);

        // Start at the head of the list
        Node current = head;

        // Check if there are no nodes in the list
        if (current == null) {
            head = newNode;
        }

        // Check if the new node data is before the head data
        else if (String.Compare(newNode.GetData(), current.GetData()) < 0) {
            // Set the new node as the head of the list
            newNode.SetNext(head);
            head = newNode;
        }

        // Otherwise find where the new node should be positioned
        else {
            // Repeat until the point of insertion is found
            while (current.GetNext() != null 
                && String.Compare(current.GetNext().GetData(), newNode.GetData()) < 0) {
                // Get the next node
                current = current.GetNext();
            }
            // Update the pointers of the new and current nodes
            newNode.SetNext(current.GetNext());
            current.SetNext(newNode);
        }
    }
}
```

---

# Quiz

What output would you expect to see in the terminal if you ran this code?
```py
class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      string_list += str(current_node.value) + "."
      current_node = current_node.next_node
    return string_list
  
a = Node(5)
b = Node(70, a)
c = Node(5675, b)
d = Node(90, c)
ll = LinkedList(d)
 
print(ll.stringify_list())
```

90.5675.70.5.

> 👏 Yes! Because the first node in ll is d and we are traversing the list from beginning to end, we would expect the values printed in this order.

Which of the following nodes is the head node of ll?

```py
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
 
class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
 
a = Node(5)
b = Node(70, a)
c = Node(5675, b)
d = Node(90, c)
ll = LinkedList(d)
```

d

> 👏 Yes! The first node, d, is the head node of the linked list.

It is possible to traverse a linked list through its list property, which keeps track of each node in the list.

True

> False <br>
> A linked list only keeps track of the first node in the list. To traverse the list, it needs a method that loops through each node to find the following node.

What is the head node in a linked list?

The first node in the list.

> 👏 Yes!

Fix the Node class so that some_node = Node(6) can run without error.

```py
class Node:
  def __init__(self, value, next_node):
    self.value = value
    self.next_node = next_node
    
some_node = Node(6)
```

Line 2 should be def __init__(self, value, next_node=None):.

> 👏 Yes!

Linked lists are made up of what elements?

Nodes

> 👏 Yes!

Consider the linked list: a -> b -> c. <br>
When removing b from the list, which node(s) need(s) to be updated?

a

> 👏 Yes! a needs to be updated to link to c.

How is a linked list terminated (in Python)?

By a node with data to None.

> By a node with a pointer to None. <br>
> The pointer itself should be set to None. Setting a node’s data to None does not impact whether or not the linked list is terminating at that node.

Given this code, what would you add to complete the .add_new_head() method?

```py
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
 
class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
    
  def add_new_head(self, new_head_node):
    # --------> what line of code goes here?
    self.head_node = new_head_node
```

new_head_node.next_node = self.head_node

> 👏 It’s necessary to set the new head node’s next_node property equal to the current list’s head node. Otherwise, you’ll lose the connection to the current head node and the rest of the linked list.

What would you add to the .remove_node() method to properly maintain the linked list when removing a node?

```py
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
 
class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
    
  def remove_node(self, node_to_remove):
    current_node = self.head_node
    if current_node == node_to_remove:
      self.head_node = current_node.next_node
    else:
      while current_node:
        next_node = current_node.next_node
        if next_node == node_to_remove:
          # --------> what line of code goes here?
          current_node = None
        else:
          current_node = next_node
```

current_node = next_node.next_node

> current_node.next_node = next_node.next_node
> This would set our current node equal to the node after next_node. To maintain the linked list we can set our current node’s next_node property equal to the node after next_node.

Linked list nodes do not contain which of the following?

Roots

> 👏 Yes!

**72%, 8 Correct, 3 to work on**