/*
 arrays are inherited from C, C++’s parent language. 
 They are a low-level data structure and are incredibly rigid. 
 With arrays, you can’t add or remove elements; you can only modify existing elements.
 Vectors are originated from arrays. Early in the creation of C++, 
 the language developers took these basic arrays and wrote code to enhance them and make them more flexible and powerful. 
 Therefore you can think of vectors as super arrays!
 */

int favoriteNums[4];
int favoriteNums[] = {7, 9, 15, 16};

char vowels[] = {'a', 'e', 'i', 'o', 'u'};
//      indexes:  0    1    2    3    4
 
std::cout << vowels[0]; // Prints: a
 
vowels[0] = 'r';
 
std::cout << vowels[0]; // Prints: r