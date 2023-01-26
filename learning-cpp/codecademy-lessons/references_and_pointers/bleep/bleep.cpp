/*
Congratulations on your new job at the Department of Re-education! 
You have been tasked with building an algorithm that can bleep out any words 
deemed unsavory by the powers that be.

Write a bleep.cpp program that “bleeps” any word that’s passed in. You’ll test 
this out with "broccoli", which has been recently banned by the Department.

Turn some text like "I'm rolling up my broccoli" into "I'm rolling up my ********".

Make sure to use pass-by-reference in your functions so you can modify the 
incoming text!
*/

// literally 1984
// literally the usa

#include <iostream>
#include <string>
#include "functions.hpp"

int main() {
    std::string word = "broccoli";
    std::string text = "broccoli is disgusting, all my homies hate broccoli";

    bleep(word, text);
    std::cout << text << "\n";
}