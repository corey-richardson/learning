#include <iostream>

int main() {

    int i = 0;
    int square = 0;

    // Write a while loop here:
    while (i <= 9){
        std::cout << i << "  " << i*i << "\n";
        i++;
    }

    for (int i = 0; i <= 9; i++){
        std::cout << i << "  " << i*i << "\n";
    }

}