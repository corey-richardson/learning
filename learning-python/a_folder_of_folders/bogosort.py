# bogosort
# this thing is disgusting

n = 1000

from itertools import permutations
from random import sample
from random import randint
import time

start = time.perf_counter()

iterations = []
for i in range(n):
    # Generate a random list
    unsorted_list = list(randint(0,100) for i in range(5))
    
    # Calculate the number of possible permutations for a list of that size
    p = permutations(unsorted_list) # creates an iterable
    count = 0
    for j in p:
        count += 1

    not_shuffled = True
    iteration = 0
    
    while not_shuffled:
        iteration += 1 # increment
        shuffled_list = sample(unsorted_list, len(unsorted_list)) # create a shuffled version of the list
        print(f"FOR REPEAT: {i+1:04d} | ATTEMPT {iteration:03d} OF {count} PERMUTATIONS | UNSORTED: {unsorted_list} | SHUFFLED: {shuffled_list} | SORTED: {sorted(unsorted_list)}")
        
        if shuffled_list == sorted(unsorted_list): # check if the randomly shuffled list is correctly sorted
            iterations.append(iteration) # if sorted, save the number of iterations it took to sort to list
            break
        
end = time.perf_counter()

# calculate average number of iterations taken to correctly sort
# should ~= number of permutations 
print("\nAvg:" , sum(iterations)/len(iterations))
print("Exp:" , count)
print("\nMin:" , min(iterations))
print("Max:" , max(iterations))

# calculate and print time data
time_taken = end - start
avg_time_taken = time_taken / n
print(f"\nAverage Time: {avg_time_taken:.5f} seconds")
print(f"Total Time: {time_taken:.5f} seconds")
