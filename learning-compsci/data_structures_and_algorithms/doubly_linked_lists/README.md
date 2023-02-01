Like a singly linked list, a doubly linked list is comprised of a series of nodes. 

Each node contains data and *two* links (or pointers) to the next and previous nodes in the list. The head node is the node at the beginning of the list, and the tail node is the node at the end of the list. The head node’s previous pointer is set to null and the tail node’s next pointer is set to null.

Think of your daily commute on the subway as a real-world example of a doubly linked list. Your home is the head of the list, your place of work is the tail, and every stop in between is another node in the list.

![doubly linked list example](https://static-assets.codecademy.com/Courses/CS102-Data-Structures-And-Algorithms/DoublyLinkedLists/CS102_DLLExample_2_M8.svg)

In a doubly linked list, adding to the list is a little complicated as we have to keep track of and set the node’s previous pointer as well as update the tail of the list if necessary.

Adding to the head

When adding to the head of the doubly linked list, we first need to check if there is a current head to the list. If there isn’t, then the list is empty, and we can simply make our new node both the head and tail of the list and set both pointers to null. If the list is not empty, then we will:

- Set the current head’s previous pointer to our new head.
- Set the new head’s next pointer to the current head.
- Set the new head’s previous pointer to null.

Adding to the tail

Similarly, there are two cases when adding a node to the tail of a doubly linked list. If the list is empty, then we make the new node the head and tail of the list and set the pointers to null. If the list is not empty, then we:

- Set the current tail’s next pointer to the new tail
- Set the new tail’s previous pointer to the current tail
- Set the new tail’s next pointer to null

---

- They are comprised of nodes that contain links to the next and previous nodes.
- They are bidirectional, meaning it can be traversed in both directions.
- They have a pointer to a single head node, which serves as the first node in the list.
- They have a pointer to a single tail node, which serves as the last node in the list.
- They require the pointers at the head of the list to be updated after addition to or removal of the head.
- They require the pointers at the tail of the list to be updated after addition to or removed of the tail.
- They require the pointers of the surrounding nodes to be updated after removal from the middle of the list.

---

`Take a moment to think about doubly linked lists. What do you think are some possible real-life uses?`
- A music player with “next” and “previous” buttons
- An app that shows you where your subway is on the train line
- The “undo” and “redo” functionality in a web browser