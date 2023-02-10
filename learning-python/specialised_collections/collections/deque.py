# lists are not optimized for appending and popping large amounts of data, 
# although they are great at accessing data at any index which you provide.
# To solve this problem, we can use deque containers. 
# These are similar to lists, but they are optimized for appending and
# popping to the front and back, rather than having optimized accessing. 
# Because of this, they are great for working with data where you don’t need 
# to access elements in the middle very often or at all.

# from collections import deque
# bug_data = deque()
# loaded_bug_reports = get_all_bug_reports()
# for bug in loaded_bug_reports:
#     if bug['priority'] == 'high':
#         bug_data.appendleft(bug)
#     else:
#         bug_data.append(bug)
# next_bug_to_fix = bug_data.popleft()

from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# First, create an empty deque called supplies_deque.
supplies_deque = deque()
# Using a for loop, read each item from csv_data. On each iteration, if the 
# item is marked as important, append it to the front of supplies_deque, 
# otherwise append it to the end.
for item in csv_data:
  if item[2] == "important":
    supplies_deque.appendleft(item)
  else:
    supplies_deque.append(item)

# Your accountant let you know that you have enough of a budget to order 25 
# important materials and 10 unimportant materials.
# For this step, create a new deque called ordered_important_supplies. 
# Remove the 25 important items from your supplies_deque and append them to 
# ordered_important_supplies.
# Now that you have completed the orders for the 25 important items, repeat 
# the same process for 10 unimportant items.
# Create a new deque called ordered_unimportant_supplies. Remove 10 low 
# important items from your supplies_deque and append them to 
# ordered_unimportant_supplies.
ordered_important_supplies = deque()
for i in range(25):
  ordered_important_supplies.append( supplies_deque.popleft() )
ordered_unimportant_supplies = deque()
for i in range(10):
  ordered_unimportant_supplies.append( supplies_deque.pop() )