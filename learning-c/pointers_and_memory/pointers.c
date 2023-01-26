#include<stdio.h>

int main() {
  // Create a double variable named dblVar.
  double dblVar;
  // Create a pointer variable called dblPtr that points to dblVar.
  double *dblPtr = &dblVar;
  // Print the address stored in dblPtr to the screen.
  printf("%p", dblPtr);
}