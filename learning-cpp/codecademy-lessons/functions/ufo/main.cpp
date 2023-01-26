/*
Invaders from outer space have arrived and are abducting humans using tractor beams.
Players must crack the codeword to stop the abduction!

Ok, we’ll admit it’s quite a bit like that classic game, “Hangman”, but with a 
better premise. Plus, building this command-line game was the Codecademy 2019 
Software Engineer Internship Backend Programming Challenge!
*/

#include <iostream>
#include "ufo_functions.hpp"

int main() {
  greet();

  std::string codeword = "hippopotomonstrosesquipedaliaphobia";
  std::string answer;
  int misses = 0;

  for (int i = 0; i < codeword.size(); i++){ // set answer to "____" where length is same as codeword 
    answer += "_";
  }

  std::vector<char> incorrect;
  bool guess = false;
  char letter;
  
  while ((answer != codeword) && (misses < 7)){
    display_misses(misses);
    display_status(incorrect, answer);

    std::cout << "Please enter your guess: ";
    std::cin >> letter;

    for (int i = 0; i < codeword.size(); i++){
      if (codeword[i] == letter) {
        answer[i] = letter;
        guess = true;
      }
    }

    if (guess) {
      std::cout << "\nCorrect! You're closer to cracking the codeword.\n";
      guess = false;
    } 
    else {
      std::cout << "\nIncorrect! The tractor beam pulls the person in further.\n";
      incorrect.push_back(letter);
      misses++;
    }
    guess = false;
  }
  end_game(answer, codeword);


}
