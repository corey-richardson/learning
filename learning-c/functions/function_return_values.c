#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getRandom1000() {
  int random1000 = rand() % 1000 + 1;
  return random1000;
}

int main(void) {
  srand(time(NULL));
  int randomNumber = getRandom1000();
  printf("My random number is: %d", randomNumber);
}