# In this exercise, we will see how we can combine the map() and filter() 
# functions.

# map(mapping_function, filter(predicate, iterable))

nums = (2, 12, 5, 8, 9, 3, 16, 7, 13, 19, 21, 1, 15, 4, 22, 20, 11)

# Given the tuple nums multiply values that are greater than 10 by two. 
greater_than_10_doubled = \
map(lambda x: x*2, filter(lambda x: x > 10, nums))
print(tuple(greater_than_10_doubled))

# Convert the following code from the imperative style to the declarative:
# IMPERATIVE:
# lst = []
# for i in nums:
#   if i % 3 == 0:
#     lst.append(i)
# for i in range(len(lst)):
#   lst[i] = lst[i] * 3
# tuple(lst)

# DECLARATIVE:
functional_way = \
map(lambda x: x*3, filter(lambda x: x % 3 == 0, nums))
print(tuple(functional_way))