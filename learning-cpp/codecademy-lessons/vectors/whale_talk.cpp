#include <iostream>
#include <vector>
#include <string>
 
int main() {
    // Whale, whale, whale.
    // What have we got here?
    // ^ comedy genius
    std::string human_talk = "turpentine and turtles";
    std::vector<char> vowels = {'a','e','i','o','u'};
    std::vector<char> result;

    for (int i = 0; i < human_talk.size(); i++){
        for (int j = 0; j < vowels.size(); j++){
            if (human_talk[i] == vowels[j]){
                result.push_back(vowels[j]);
                if (vowels[j] == 'e' || vowels[j] == 'u') {
                    result.push_back(vowels[j]);
                }
            }
        }
    }
    for (int i = 0; i < result.size(); i++){
        std::cout << result[i];
    }
}