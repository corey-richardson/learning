// a pointer stores a memory address.

/*
int* number;
double* decimal;
char* character;

// So suppose we have a variable called gum:
int gum = 8;

// We can create a pointer to it by:
int* ptr = &gum;

int* makes it a pointer rather than a normal variable.
ptr is the pointer name.
&gum is the memory address of the other variable gum.
*/

#include <iostream>
int main() {
    int power = 9000;
    // Create pointer
    int* ptr = &power;
    // Print ptr
    std::cout << ptr;
}