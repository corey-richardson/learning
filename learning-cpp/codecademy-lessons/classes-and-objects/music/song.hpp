#include <string>

class Song {
  
    // attributes
    std::string title;

// methods
/* 
By default, everything in a class is private, meaning class members are limited 
to the scope of the class. This makes it easier to keep data from mistakenly 
being altered, and abstracts away all the nitty gritty details. If you try to 
access a private class member, you’ll get an error.

But sometimes you need access to class members, and for that, there is public.

There is also a private access modifier for when you want something below 
public to be private to the class

class City {
  int population; 
public:
  void add_resident() { 
    population++;
  }
private: // this stuff is private
  bool is_capital;
};

*/
public:
    /*
    A constructor is a special kind of method that lets you decide how the objects 
    of a class get created. It has the same name as the class and no return type. 
    Constructors really shine when you want to instantiate an object with specific 
    attributes.

    City::City(std::string new_name, int new_pop) {
    name = new_name;
    population = new_pop; 
    }    
    */
    
    Song(std::string new_title, std::string new_artist);


    void add_title(std::string new_title);
    std::string get_title();

    void add_artist(std::string new_artist);
    std::string get_artist();

    ~Song(); // destructor

};
