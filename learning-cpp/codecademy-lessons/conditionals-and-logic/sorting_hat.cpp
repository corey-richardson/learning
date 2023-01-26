#include <iostream>
 
int main() {
  int gryffindor = 0;
  int hufflepuff = 0;
  int ravenclaw  = 0;
  int slytherin  = 0;
  int answer1, answer2, answer3, answer4;

  std::cout << "The Sorting Hat Quiz!\n";

  // q1
  std::cout << "Q1) When I'm dead, I want people to remember me as:\n\n";
  std::cout << "1) The Good\n";
  std::cout << "2) The Great\n";
  std::cout << "3) The Wise\n";
  std::cout << "4) The Bold\n";
  std::cin >> answer1;
  switch (answer1){
    case 1:
      hufflepuff++;
      break;
    case 2:
      slytherin++;
      break;
    case 3:
      ravenclaw++;
      break;
    case 4:
      gryffindor++;
      break;

    default:
      std::cout << "Invalid Input\n";
  }

  // q2
  std::cout << "Q2) Dawn or dusk?\n\n";
  std::cout << "1) Dawn\n";
  std::cout << "2) Dusk\n";
  std::cin >> answer2;
  switch (answer2){
    case 1:
      gryffindor++;
      ravenclaw++;
      break;
    case 2:
      hufflepuff++;
      slytherin++;
      break;

    default:
      std::cout << "Invalid Input\n";
  }

  // q3
  std::cout << "Q3) Which kind of instrument most pleases your ears?\n\n";
  std::cout << "1) The violin\n";
  std::cout << "2) The trumpet\n";
  std::cout << "3) The piano\n";
  std::cout << "4) The drum\n";
  std::cin >> answer3;
  if (answer3 == 1){
    slytherin++;
  }
  else if (answer3 == 2){
    hufflepuff++;
  }
  else if (answer3 == 3){
    ravenclaw++;
  }
  else if (answer3 == 4){
    gryffindor++;
  }
  else{
    std::cout << "Invalid input\n";
  }

  // q4
  std::cout << "Q4) Which road tempts you most?\n\n";
  std::cout << "1) The wide, sunny grassy lane\n";
  std::cout << "2) The narrow, dark, lantern-lit alley\n";
  std::cout << "3) The twisting, leaf-strewn path through woods\n";
  std::cout << "4) The cobbled street lined (ancient buildings)\n";
  std::cin >> answer4;

  if (answer4 == 1) {hufflepuff++;}
  else if (answer4 == 2) {slytherin++;}
  else if (answer4 == 3) {gryffindor++;}
  else if (answer4 == 4) {ravenclaw++;}
  else {std::cout << "Invalid input";}

  // results
  int max = 0;
  std::string house;

  if (gryffindor > max) 
  {
    max = gryffindor;
    house = "Gryffindor";
  }
  
  if (hufflepuff > max) 
  {
      max = hufflepuff;
      house = "Hufflepuff";
  }
  
  if (ravenclaw > max) 
  {
      max = ravenclaw;
      house = "Ravenclaw";
  }
  
  if (slytherin > max) 
  {
      max = slytherin;
      house = "Slytherin";
  }
  
  std::cout << house << "!\n";
  return 0;
}