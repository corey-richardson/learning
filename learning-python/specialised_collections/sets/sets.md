Creating a set or frozenset:
- For set containers, we can use curly braces {}, the set() constructor, or set comprehension.
- For frozenset containers, we can only use the frozenset() constructor.

Adding items to a set:
- We can add items to a set individually using the .add() method.
- We can add multiple items at once using the .update() method.

Removing items from a set:
- The .remove() method is used to remove elements from a set.
- The .discard() method can also be used to remove elements from a set. It does not throw a KeyError if the element is not found.

Finding Elements:
- The in keyword can be used with set and frozenset containers to test if an element exists inside of them.

Union:
- A union can be found using set or frozenset containers with the .union() method or | operator.

Intersection:
- An intersection can be found using set or frozenset containers with the .intersection() method or & operator.

Difference:
- The difference can be found using set or frozenset containers with the .difference() method or - operator.

Symmetric Difference:
- The symmetric difference can be found using set or frozenset containers with the .symmetric_difference() method or ^ operator.