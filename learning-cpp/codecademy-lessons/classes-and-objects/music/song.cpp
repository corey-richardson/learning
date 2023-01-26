#include "song.hpp"
#include <iostream>

Song::Song(std::string new_title, std::string new_artist){
  title = new_title;
  artist = new_artist;
}

void Song::add_title(std::string new_title) {
  title = new_title;
}

std::string Song::get_title() {
  return title;
}

void Song::add_artist(std::string new_artist) {
  artist = new_artist;
}

std::string Song::get_artist() {
  return artist;
}

Song::~Song(){ // have to include <iostream>
    std::cout << "Goodbye " << title;
}