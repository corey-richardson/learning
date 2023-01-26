/*
The asterisk sign * a.k.a. the dereference operator is used to obtain the value 
pointed to by a variable. This can be done by preceding the name of a pointer
variable with *.

int blah = *ptr;

When * is used in a declaration, it is creating a pointer.
When * is not used in a declaration, it is a dereference operator.
*/

#include <iostream>

int main() {
    //Create variable
    int power = 9000;
    // Create pointer
    int* ptr = &power;
    // Print ptr
    std::cout << ptr << "\n";
    // Print *ptr
    std::cout << *ptr << "\n";
}