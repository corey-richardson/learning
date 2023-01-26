/*
Up to this point when a function has received an argument, the function makes a 
copy of the argument’s value and stores it in the parameter variable. Now any 
work that the function does on that parameter variable will not affect the 
original value passed in.


```
#include <stdio.h>
 
void myFunc(int a){
  a = a + 2;
  printf("a inside myFunc(): %d\n", a);
}
 
int main(){
  int a = 10;
  myFunc(a);
  printf("a in main(): %d\n", a);
}
```

//OUTPUT:
// a inside myFunc(): 12;
// a in main(): 10;

This is great because we can safely alter the variable value inside the 
function while maintaining the original value outside.

What if we want to alter the variable inside the function? Instead of 
passing the actual variable as an argument, we can pass a pointer to the 
variable. Remember, a pointer is a variable that holds the memory address 
to another variable. The memory address tells you where the original 
variable is in memory.
*/

#include <stdio.h>

void incrementAge(int* agePointer){
  *agePointer += 1;
}

int main(void) {
  int age = 18;

  printf("%i\n", age);
  incrementAge(&age);
  printf("%i\n", age);
}