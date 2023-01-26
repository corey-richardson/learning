#include <iostream>
/*
You just returned from a trip to South America. The countries you visited were Colombia, Brazil, and Peru. You arrived back in your country with some foreign currencies from these three countries.
Write a C++ program called currency.cpp that prompts the user for the amount of each foreign currency.
Your program should then convert the amount entered by the user and display the total amount of USD.
*/
int main() {
  double pesos, reais, soles;
  double dollars;
  
  std::cout << "Enter number of Columbian Pesos: ";
  std::cin >> pesos;
  std::cout << "Enter number of Brazilian Reais: ";
  std::cin >> reais;
  std::cout << "Enter number of Peruvian Soles: ";
  std::cin >> soles;
  // 1 Colombian Peso equals 0.00021 United States Dollar
  // 1 Brazilian Real equals 0.19 United States Dollar
  // 1 Sol equals 0.26 United States Dollar

  dollars = (0.00021 * pesos) + \
  (0.19 * reais) + \
  (0.26 * soles);

  std::cout << "US Dollars = $" << dollars << "\n";
}