# When working with a file that contains a large amount of data, generating 
# every possible record using tuple() is inefficient. Recall from the previous 
# exercise that map() returns an iterator that we can use to bring in data. 
# We can apply the higher-order functions to this iterator to process the data
# and only bring in the relevant set of records.

import csv
from collections import namedtuple
from functools import reduce

tree = namedtuple("tree", ["index", "width", "height", "volume"]) 

with open('trees.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader)
  mapper = \
      map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), \
          reader)
  
  # Create a tuple called trees and populate it with data of trees that have a
  # height greater than 75.
  # First, create an iterator called t where you filter out trees that don’t
  # meet the height requirement. 
  t = filter(lambda h: h.height > 75, mapper)
  trees = tuple(t)

  # Create a variable called widest and store in it the record of the widest 
  # tree in trees.
  widest = reduce(lambda x,y: x if x > y else y, trees)

  print(widest)
  # tree(index=31, width=20.6, height=87, volume=77.0)