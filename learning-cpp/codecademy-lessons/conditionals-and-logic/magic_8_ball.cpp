#include <iostream>
#include <cstdlib>
 
int main() {
  std::cout << "MAGIC 8-BALL:\n";

  // Generate random number 0-10
  srand(time(NULL)); // seed
  int answer = std::rand() % 10;
  std::cout << answer << ": ";

  if (answer == 0){
    std::cout << "It is certain";
  }
  else if (answer == 1){
    std::cout << "It is decidedly so.";
  }
  else if (answer == 2){
    std::cout << "Without a doubt.";
  }
  else if (answer == 3){
    std::cout << "Yes - definitely.";
  }
  else if (answer == 4){
    std::cout << "As I see it, yes.";
  }
  else if (answer == 5){
    std::cout << "Most likely.";
  }
  else if (answer == 6){
    std::cout << "Signs point to yes.";
  }
  else if (answer == 7){
    std::cout << "Cannot predict now.";
  }
  else if (answer == 8){
    std::cout << "Better not tell you now.";
  }
  else if (answer == 9){
    std::cout << "My sources say no.";
  }
  else if (answer == 10){
    std::cout << "Outlook not so good";
  }
  else {
    std::cout << "Very doubtful";
  }
}