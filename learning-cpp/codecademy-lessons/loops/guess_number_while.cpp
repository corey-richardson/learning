#include <iostream>

int main() {

  // Guess
  int guess;
  int tries = 0;
  std::cout << "I have a number 1-10.\n";
  std::cout << "Please guess it: ";
  std::cin >> guess;
 
  while (guess != 8 && tries < 50){
    std::cout << "Wrong guess, try again: ";
    std::cin >> guess;
    tries++;
  }
  if (guess == 8) {
    std::cout << "You got it!\n";
  }  

  
}