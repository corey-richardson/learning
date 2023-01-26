template <typename T>
T get_smallest(T num1, T num2) { 
  return num2 < num1? num2 : num1;
}

/*

REPLACES OVERLOAD IN .CPP:

int get_smallest(int num1, int num2) {
  return num2 < num1? num2 : num1;
}

double get_smallest(double num1, double num2) {
  return num2 < num1? num2 : num1;
}

*/