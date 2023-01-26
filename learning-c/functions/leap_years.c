#include <stdio.h>
#include <stdbool.h>

// function prototypes
bool isLeapYear(int);

int main() {
  /*
  // Test prints                    // Outputs
  printf("%d\n", isLeapYear(2000)); // 1
  printf("%d\n", isLeapYear(2001)); // 0
  printf("%d\n", isLeapYear(2004)); // 1
  printf("%d\n", isLeapYear(2400)); // 1
  */
  int year;
  printf("Enter a year between 1800 and 10000:\n");
  scanf("%i", &year);
  if (isLeapYear(year)){ printf("Leap Year\n");
  } else { printf("Not Leap Year\n"); }
}

bool isLeapYear(int year){
  // A leap year has to be divisible by 4 and NOT divisible by 100 except when the year is divisible by 400.
  if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
    // is divisible by 4
    // isnt divisible by 100 UNLESS it is also divisible by 400
    return true;
  } else { return false; }
}
