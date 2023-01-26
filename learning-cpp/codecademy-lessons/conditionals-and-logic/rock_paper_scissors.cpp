/*
Scissors cuts Paper.
Paper covers Rock.
Rock crushes Lizard.
Lizard poisons Spock.
Spock smashes Scissors.
Scissors decapitate Lizard.
Lizard eats Paper.
Paper disproves Spock.
Spock vaporizes Rock.
(and as it always has) Rock crushes Scissors.
*/

#include <iostream>
#include <stdlib.h>
int main() {
  srand(time(NULL)); // seed
  int computer = rand() % 3 + 1;
  int user = 0;
  std::cout << "====================\n";
  std::cout << "rock paper scissors!\n";
  std::cout << "====================\n";
  std::cout << "1) ✊\n";
  std::cout << "2) ✋\n";
  std::cout << "3) ✌️\n";
  std::cout << "shoot! ";

  std::cin >> user;

  if (user == 1){ // rock
    std::cout << "Rock!\n";
    switch (computer){
      case 1:
        std::cout << "Rock: Tie!";
        break;
      case 2:
        std::cout << "Paper: Computer wins!";
        break;
      case 3:
        std::cout << "Scissors: You win!";
        break;
    }
  }
  else if (user == 2){ // paper
    std::cout << "Paper!\n";
    switch (computer){
      case 1:
        std::cout << "Rock: You win!";
        break;
      case 2:
        std::cout << "Paper: Tie!";
        break;
      case 3:
        std::cout << "Scissors: Computer wins!";
        break;
    }
  }
  else if (user == 3){ // scissors
    std::cout << "Scissors!\n";
    switch (computer){
      case 1:
        std::cout << "Rock: Computer wins!";
        break;
      case 2:
        std::cout << "Paper: You win!";
        break;
      case 3:
        std::cout << "Scissors: Tie!";
        break;
    }
  }
  std::cout << "\n";
  
}