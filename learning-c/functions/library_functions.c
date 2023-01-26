/*
ceil(): takes any number as an argument, rounds it up to the nearest integer, and returns the integer.
log(): takes an integer as an argument and returns the natural logarithm of the given number.
toupper(): takes a char as an argument and returns the uppercase of any alphabetic character.
isupper(): takes a char as an argument and returns 1 if the character is an uppercase letter, 0 otherwise.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
  srand(time(NULL)); // seeder
  int randomNumber = rand() % 20 + 1; // 1-20
  printf("%i\n", randomNumber);
  
}