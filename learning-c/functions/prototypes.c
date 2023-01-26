#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Instead of making sure our functions are always declared above where they are called, a good practice is to define function prototypes at the top of our code:

void repeatDigit(int);
int getRandomNumber(int);

int main(void) {
  srand(time(NULL));
  int repetitions = getRandomNumber(10);
  repeatDigit(repetitions);
}

// BELOW MAIN

void repeatDigit(int repetitions) {
  int digit = getRandomNumber(9);
  for(int i = 0; i < repetitions; i++) {
    printf("%d ", digit);
  }
  printf("\n");
}

int getRandomNumber(int maxNumber) {
  int randomNumber = rand() % maxNumber + 1;
  return randomNumber;
}


