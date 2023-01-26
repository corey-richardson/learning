/*
In the lesson on strings, you learned about the strcpy() function that is used 
to copy one string into another string. Recall that strcpy() requires two 
strings: one source string and one destination string. It will copy the 
contents of the source string into the destination string.

In this project, you will increase your understanding of this function by 
implementing its functionality. You will see how strcpy() works “under the 
hood.”

In your code, you will implement the strcpy() functionality inside the 
copy() function. You will do this by using your knowledge about pointers.

Recall that a string is an array of type char. Also, recall that an array 
can be traversed using a pointer. A pointer to an array (or string) 
initially points to the first element (or character) in the array (string).

The concept of a function will be covered in a later lesson, so don’t worry 
too much about the details of how a function works. For now, just think of a 
function as a way to neatly organize your code.

Inside the copy() function, the char pointer src is pointing to the address 
of the first character in the source string, and the dst pointer is pointing 
to the first character of the destination string.
*/

#include<stdio.h>
#include<string.h>
 
void copy(char* dst, char* src){
    while (src != "\0") {
        *dst = *src;
        src++;
        dst++;
    }
    *dst = '\0';
}
 
int main(){
    char srcString[] = "We promptly judged antique ivory buckles for the next prize!";
    char dstString[strlen(srcString + 1)];
    strcpy(dstString, srcString);
    printf("%s", dstString);
}