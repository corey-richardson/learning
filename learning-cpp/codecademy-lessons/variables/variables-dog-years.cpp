#include <iostream>

int main() {
  int dog_years = 10;
  int early_years = 21;
  int later_years = (dog_years - 2) * 4;
  int human_years = early_years + later_years;
  
  std::cout << "My name is Cat! Ruff ruff, I am " << human_years << " years old in human years.\n";
  
}