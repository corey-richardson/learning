/*
When we declare a pointer variable like so, its content is not intialized:
int* ptr;

In other words, it contains an address of “somewhere”, which is of course 
not a valid location. This is dangerous! We need to initialize a pointer by 
assigning it a valid address.

But suppose we don’t know where we are pointing to, we can use a null pointer.

nullptr is a new keyword introduced in C++11. It provides a typesafe pointer 
value representing an empty pointer.

We can use nullptr like so:
int* ptr = nullptr;

*/

#include <iostream>

int main() {
    int power = 9000;
    // Create pointer
    // int* ptr; <-- bad
    int* ptr = nullptr;
    // Later in the program...
    ptr = &power;
    // Print ptr
    std::cout << ptr << "\n";
}