from functools import reduce

costs = \
{"shirt": (4, 13.00), 
 "shoes":(2, 80.00), 
 "pants":(3, 100.00), 
 "socks":(5, 5.00), 
 "ties":(3, 14.00), 
 "watch":(1, 145.00)}

nums = \
(24, 6, 7, 16, 8, 2, 3, 11, 21, 20, 22, 23, 19, 12, 1, 4, 17, 9, 25, 15)

# Given the record of item sales costs, find the total cost of items that cost 
# more than £150.
total = \
reduce(lambda x,y: x+y, \
filter(lambda x: x > 150, \
map(lambda n: costs[n][0] * costs[n][1], costs)))

print(total)


# Given the tuple nums, use map(), filter(), and reduce() to find all numbers
# less than 10, add five to them, and find their total product
product = \
reduce(lambda x,y: x*y, \
map(lambda a: a+5, \
filter(lambda z: z < 10, nums)))

print(product)