#include<stdio.h>

int main() {
  
  int k = 2000;
  int* ptr = &k;
  
  // Print the data stored in the memory address that ptr is pointing to.
  printf("%i\n",*ptr);
  // Change the value contained in the memory address pointed to by ptr from 2000 to 961.
  *ptr = 961;
  printf("%i\n", k); // Notice how this variable changed value after Checkpoint 2!
}
