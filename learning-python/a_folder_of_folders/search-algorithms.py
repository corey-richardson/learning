# Search algorithms

# Generate list
def generate_list(sort_type):
    import random
    # Gets the user input for length_of_list
    # If a non-int value is enterred then the user will be reprompted until they
    # enter valid input
    while True:
        length_of_list = input("%s: How long should the list be? " % sort_type)
        try:
            length_of_list = int(length_of_list)
            break
        except ValueError:
            print("Inputted value should be in int format.")
    # Returns a list of random numbers using list comprehension     
    return [random.randint(0,100) for i in range(length_of_list)]
# -------------

# Print list and target
def print_list_and_target(number_list,target_number):
    print("List: " + str(number_list))
    print("Target value: " + str(target_number))
# -------------

# Linear Search
def linear_search(search_list,target_value):
    # Initialises list of matches and maximum_score_index
    matches = []
    maximum_score_index = None
    # Iterates through each index in the list
    for i in range(len(search_list)):
        # If the value is equal to the target value then the index is appended to the list 
        # of matches
        if search_list[i] == target_value:
            matches.append(i)
        # If the current value is greater than the previous maximum value, or the default value of "None" then
        # the values index is set as the maximum_score_index
        if maximum_score_index == None or search_list[i] > search_list[maximum_score_index]:
            maximum_score_index = i
    # If a match has been found:
    if len(matches) != 0:
        print("The largest number in the list is at index %i, with a value of %i." % (maximum_score_index,search_list[maximum_score_index]))
        return matches
    # If no match is found:
    # this shouldn't come up because the target value is selected from the list
    # if it does then uh oh?
    else:
        raise ValueError("%s not in list" % str(target_value))
# -------------

# Binary Search
def binary_search(number_list,target_number):
    # If list is empty, return "value not found" because cleary something hasn't worked
    if len(number_list) == 0:
        return "value not found"
    # Calculate the middle index of the list and get the corresponding value
    # int(len(number_list)/2)
    mid_idx = len(number_list) // 2
    mid_val = number_list[mid_idx]
    # If middle value is the target, target has been found --> return the index it was found at
    if mid_val == target_number:
        return mid_idx
    # Else if the middle value is too large, assume the target is to the left of the value
    # Create a new list "left" which contains all values less than the middle value
    if mid_val > target_number:
        left = number_list[:mid_idx]
        # Recursion
        # The left list is now the one being compared instead of the full list
        return binary_search(left,target_number)
    # Else if the middle value is too small, assume the target is to the righ of the value
    # Create a new list "right" which contains all values less than the middle value
    if mid_val < target_number:
        right = number_list[mid_idx+1:]
        result = binary_search(right,target_number)
        # if the recursion results in "value not found", somethings gone wrong
        # break
        if result == "value not found":
            return result
        else:
            return result + mid_idx + 1
# -------------

# test_search
# uses the python in built search feature to check the algorithm values are correct
# limitations: only outputs the first instance
def test_search(number_list,target_number):
    print("ACTUAL: %i @ index %i" % (target_number,number_list.index(target_number)))
# -------------
# Main
def main():
    from random import choice
    # Linear Search
    # Unsorted list 
    # Generates a list of random numbers       
    number_list = generate_list("Linear")
    # From the generated list, choose a random number to be the target value
    target_number = choice(number_list)
    # Print the list and the target to the user
    print_list_and_target(number_list,target_number)
    # Print any matches found to the user
    print("Matches of target %i found at index/es: %s" % (target_number,str(linear_search(number_list,target_number))))
    test_search(number_list,target_number)
    print("")
    
    # Binary Search
    # Sorted list, for now I will use .sort() however I can expand on this in the future with a sort algorithm
    # Generates a list of random numbers
    number_list = generate_list("Binary")
    # From the list, select a random number to act as the target value
    target_number = choice(number_list)
    # Sort the list (binary search needs a sorted list)
    # ADD A SORT ALGORITHM HERE
    number_list.sort()
    # Print the list and the target to the user
    print_list_and_target(number_list,target_number)
    # Outputs the location of the value
    print("Match of target %i found at index %i" % (target_number,binary_search(number_list,target_number)))
    test_search(number_list,target_number)
    print("")
# -------------
    
main()

# Iterative binary search
# def binarySearch(sorted_list, search_value):
  
#   left_pointer = 0
#   right_pointer = len(sorted_list) - 1
#   while left_pointer <= right_pointer:
#     mid_pointer = (left_pointer + right_pointer) // 2
#     if search_value == sorted_list[mid_pointer]:
#       return mid_pointer
#     if search_value < sorted_list[mid_pointer]:
#       right_pointer = mid_pointer - 1
#     if search_value > sorted_list[mid_pointer]:
#       left_pointer = mid_pointer + 1
  
#   return "Value not in list"