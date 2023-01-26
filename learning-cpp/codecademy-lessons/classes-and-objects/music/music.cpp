#include <iostream>
#include "song.hpp"

int main() {

    Song electric_relaxation; // insantiate object
    electric_relaxation.add_title("Electric Relaxation"); // set title
    std::cout << electric_relaxation.get_title(); // get title and output

    Song back_to_black("Back to Black","Amy Winehouse");

    std::cout << back_to_black.get_title() << " by " << back_to_black.get_artist();
    

}