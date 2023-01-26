// ( 1 < 2 && 2 < 3 ) returns true
// ( 1 < 2 && 2 > 3 ) returns false
// ( 1 < 2 || 2 > 3 ) returns true

#include <iostream>

int main() {
  
    // AND &&
    int hunger = true;
    int anger = true;
    if (hunger && anger){
        std::cout << "Hangry\n";
    }

    // OR ||
    int day = 6;
    if (day == 6 || day == 7){
        std::cout << "Weekend\n";
    }

    // NOT !
    // ( !true ) returns false
    // The keyword not can be used in the place of !
    bool logged_in = false;
    if (not(logged_in)){
        std::cout << "Try again\n";
    }
}