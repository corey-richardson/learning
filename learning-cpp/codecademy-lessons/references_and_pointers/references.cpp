/*
In C++, a reference variable is an alias for something else, that is, another
name for an already existing variable.

We make Sonny a reference to someone named Songqiao. You can refer to the 
person as either Sonny or Songqiao.
Let’s take a look at how we can do this with code. Suppose we have an int
variable already called songqiao, we can create an alias to it by using 
the & sign in the declaration:

int &sonny = songqiao;

Anything we do to the reference also happens to the original.
Aliases cannot be changed to alias something else.
*/

// alias

#include <iostream>

int main() {

    int soda = 99;
    int &pop = soda;

    pop++;
    std::cout << pop << "\n" << soda;

}