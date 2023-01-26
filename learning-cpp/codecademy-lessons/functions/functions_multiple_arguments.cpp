#include <iostream>

void name_x_times(std::string name, int x){
  while (x > 0){
    std::cout << name << "\n";
    x--;
  }
}

int main() {
  std::string my_name = "Corey";
  int some_number = 10;

  name_x_times(my_name,some_number);
  std::cout << "\n";
  name_x_times("Corey",10);
}