/*
The only arithmetic operations allowed for pointers are addition and subtraction.
The addition operation for a pointer is only valid when adding an integer to a 
pointer; you cannot add two or more pointers together!

ptr += 3; // Increment pointer by three blocks. 

*/

#include<stdio.h>

int main() {
  double* ptr1;

  // Increment the double pointer ptr1 by five.
  ptr1 += 5;
  // Decrement the pointer ptr1 by four.
  ptr1 -= 4;  
}