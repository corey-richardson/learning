/*
return_type function_name( any, parameters, you, have ) {
   // Code block here
   return output_if_there_is_any;
 
}
*/

void make_sandwich() { // procedure
    std::cout << "bread\n";
    std::cout << "egg\n";
    std::cout << "cheese\n";
    std::cout << "avocado\n";
    std::cout << "bread\n";
}

void oscar_wilde_quote(){ // procedure
    std::cout << "The highest, as the lowest, form of criticism is a mode of autobiography.";
}

std::string always_blue() { // function
    return "blue!\n";
}

bool needs_it_support() { // function, returns true/false value
    bool support;
    std::cout << "Hello. IT. Have you tried turning it off and on again? Enter 1 for yes, 0 for no.\n";
    std::cin >> support;
    return support;
}

int main {
    make_sandwich();
    oscar_wilde_quote();
    always_blue();
    std::cout << needs_it_support();
}