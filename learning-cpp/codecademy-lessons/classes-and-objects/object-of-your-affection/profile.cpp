#include "profile.hpp"
#include <iostream>

Profile::Profile(
    std::string new_name,
    int new_age,
    std::string new_city,
    std::string new_country,
    std::string new_pronouns){
        name = new_name;
        age = new_age;
        city = new_city;
        country = new_country;
        pronouns = new_pronouns;
        }

std::string Profile::view_profile() {
 
    std::string bio = "Name: " + name;
    bio += "\nAge: " + std::to_string(age);
    bio += "\nLocation: " + city + ", " + country;
    bio += "\nPronouns: " + pronouns;

    bio += "\nHobbies:\n";
    for (int i = 0; i < hobbies.size(); i++){
        bio += "- " + hobbies[i] + "\n";
    }
    bio += "\n";

    return bio;

}

void Profile::add_hobby(std::string new_hobby){
    hobbies.push_back(new_hobby);
}