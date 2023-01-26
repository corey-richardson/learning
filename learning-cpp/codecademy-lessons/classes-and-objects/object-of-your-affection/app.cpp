#include <iostream>
#include "profile.hpp"

int main() {
    Profile sam("Sam Drakkila",30,"New York","USA","he/him");
    sam.add_hobby("archery");
    sam.add_hobby("having crisises");
    sam.add_hobby("not thriving");

    std::cout << sam.view_profile();

}