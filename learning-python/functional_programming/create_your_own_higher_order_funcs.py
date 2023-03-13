# To further your understanding of functional programming, you will create your
# own higher-order functions and then use them to process data from a CSV file.
# The functions you will create are:
# count(): will return the frequency of an element in an iterable
# average(): will return the average of elements in an iterable of numbers

import csv
from functools import reduce

def count(predicate, itr):
  # Inside the count() function, write a filter() function that will “filter”
  # itr based on predicate. Save this value to a variable called count_filter.
  count_filter = filter(predicate, itr)
  # Inside of count(), use reduce() to process the iterator returned from 
  # filter() so the accumulator imcrements by one for each True evaluation
  # from filter().
  count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
  return count_reduce

def average(itr):
  iterable = iter(itr)
  # make the initial call to avg_helper() with the proper initial values for
  # curr_count and curr_sum. Return the value found by avg_helper().
  return avg_helper(0, iterable, 0)

# create the average() function that will compute an average recursively.
def avg_helper(curr_count, itr, curr_sum): 
  # Use next() to obtain the next value in the iterable. Set this value to a
  # variable called next_num. Add this value to curr_sum.
  next_num = next(itr, "null")
  # the loop should terminate when all the elements in the iterable are 
  # processed; i.e., next() returns "null". When next() returns "null", 
  # avg_helper() should compute the average and return that value.
  if next_num == "null": 
    return curr_sum/curr_count
  curr_count += 1 
  curr_sum += next_num
  # Call avg_helper() in the proper location and return the value.
  return avg_helper(curr_count, itr, curr_sum)


with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  # Replace count_belgiums = None with your count() function.
  count_belgiums = count(lambda x: x[1] == "Belgium", reader)
  print(count_belgiums)
  csvfile.seek(0)
  # Use your average() function to compute the average total profit 
  # (index 13) for Portugal.
  avg_portugal = average(map(lambda x: float(x[13]),filter(lambda x: x[1] == "Portugal", reader)))
  print(avg_portugal)

  
# Typically, recursive functions follow this style:

# def recursive_function():
#   # Base Case
#   # Computation
#   # Recursive call
