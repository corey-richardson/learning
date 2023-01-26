/*
Pass-by-reference refers to passing parameters to a function by using references. 
When called, the function can modify the value of the arguments by using the 
reference passed in.

This allows us to:
Modify the value of the function arguments.
Avoid making copies of a variable/object for performance reasons.

    void swap_num(int &i, int &j) {
    
    int temp = i;
    i = j;
    j = temp;
    
    }
    
    int main() {
    
    int a = 100;
    int b = 200;
    
    swap_num(a, b);
    
    std::cout << "A is " << a << "\n";
    std::cout << "B is " << b << "\n";
    
    }

int &i and int &j are the parameters of the function swap_num().
When swap_num() is called, the values of the variables a and b will be 
modified because they are passed by reference.

Suppose we didn’t pass-by-reference here and have the parameters as simply 
int i and int j in the swap_num() function, then i and j would swap, but a 
and b wouldn’t be modified.

To reiterate, using references as parameters allows us to modify the arguments’
values. This can be very useful in a lot cases.
*/

#include <iostream>

int triple(int &i) { // pass-by-reference
    i = i * 3;
    return i;
}

int main() {
    int num = 1;
    std::cout << triple(num) << "\n";
    std::cout << triple(num) << "\n";
}

// when the parameter is "int i", output is 3, 3
// when the parameter is "int &i", output is 3, 9