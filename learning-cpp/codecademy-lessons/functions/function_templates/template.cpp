// in hpp
template <typename T>
void print_cat_ears(T item) {
 
  std::cout << " " << item << "   " << item << " " << "\n";
  std::cout << item << item << item << " " << item << item << item << "\n";
 
}

// We can call the function for int, char, std::string, or double:

print_cat_ears(2);
print_cat_ears('C');