#include <iostream>
#include <vector>

std::vector<int> first_three_multiples(int num){
  std::vector<int> f;
  f.push_back(num);
  f.push_back(num*2);
  f.push_back(num*3);
  return f;
}

int main() {
  for (int element : first_three_multiples(8)) {
    std::cout << element << "\n";
  }
}