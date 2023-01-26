#include <iostream>

int main() {
  int year;
  std::cout << "Enter year: ";
  std::cin >> year;

  // 4 digit = 1000-->9999
  if ( !(year >= 1000 && year <= 9999) ){
    std::cout << "Invalid\n";
  }
  else{
    if (not(year % 400 == 0) && year % 4 == 0){
      std::cout << "Leap year\n";
    }
    else{
      std::cout << "Not a leap year\n";
    }
  }
}

/*
$ g++ leap_year.cpp -o leap_year
$ ./leap_year 
Enter year: 2000
Not a leap year
$ ./leap_year 
Enter year: 2004
Leap year
$ ./leap_year 
Enter year: 12345
Invalid
*/