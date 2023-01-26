/*
To avoid wastage of memory, you can dynamically allocate any memory required 
during runtime using the new and delete operators in C++.
*/

int main() {
 
  // memory allocation
  ptr = new int[num];
 
  ...
 
  // memory is released
  delete ptr;
 
}

ptr = new int[num];
delete ptr;

/*
If you create something with new, at some point you must delete it. 
When something is not deleted, it will cause a memory leak.

The rule of three is a rule of thumb in C++ that claims that if a class defines one of the following special member functions, it should define all three:
Destructor
Copy constructor
Copy assignment operator

With C++11, a new rule emerged: the rule of five. This adds two more special functions to the rule of three list:
Destructor
Copy constructor
Copy assignment operator
Move constructor
Move assignment operator
*/

