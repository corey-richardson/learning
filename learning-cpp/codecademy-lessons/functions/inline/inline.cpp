/*
Using inline advises the compiler to insert the function’s body where the function
call is, which sometimes helps with execution speed (and sometimes hinders execution
speed). If you do use it, we recommend testing how it affects the execution speed
of your program. The bottom line is inline is something you’ll probably encounter,
but may never use.

However, you will sometimes also hear about “inline functions” that are just member
functions (i.e. functions inside of classes — we’ll explain classes later) which 
have been defined and declared in a single line in a header file because the 
function body is so short:

    // cookie_functions.hpp
    
    // eat() belongs to the Cookie class:
    void Cookie::eat() {std::cout << "nom nom\n";} 

Please note that you should ALWAYS add the inline keyword if you are inlining 
functions in a header (unless you are dealing with member functions, which are 
automatically inlined for you).
*/