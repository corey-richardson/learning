#include<stdio.h>

int main() {
  
  double g = 9.81;
  double pi = 3.14;
  
  // Declare a pointer to a double called dblPtr and assign to it the address of variable g.
  double *dblPtr = &g;
  // Print the address of variable g.
  printf("%p\n",dblPtr);
  // Reassign dblPtr to the address of the variable pi.
  dblPtr = &pi;
}