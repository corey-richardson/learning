#include <iostream>
#include <vector> // INCLUDE VECTORS

int main() {

    // std::vector<type> name;
    std::vector<double> subway_adult;
    std::vector<double> subway_child;

    std::vector<double> location = {42.651443, -73.749302};

    // another way we can initialize our vector is by presizing
    // we want to create and initialize a vector with two elements
    // we don’t know what values we want to add yet
    std::vector<double> location(2);
    // defaults to {0.0, 0.0}

    // indexing
    std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    index_2 = vowels[2]
    std::cout << vowels[0] << "\n"; // a
    std::cout << vowels[1] << "\n"; // e
    std::cout << vowels[2] << "\n"; // i
    std::cout << vowels[3] << "\n"; // o
    std::cout << vowels[4] << "\n"; // u

    // add elements using .push_back()
    std::vector<std::string> dna = {"ATG", "ACG"};
    dna.push_back("GTG");
    dna.push_back("CTG");
    // ATG ACG --> ATG ACG GTG CTG

    // remove elements from the “back” of the vector using .pop_back()
    dna.pop_back();
    // ATG ACG GTG CTG --> ATG ACG GTG

    // size
    std::vector<std::string> grocery = {"Hot Pepper Jam", "Dragon Fruit", "Brussel Sprouts"};
    std::cout << grocery.size() << "\n";
  
    // string vector
    std::vector < std::string > airports = {"JFK", "PVG"}
}