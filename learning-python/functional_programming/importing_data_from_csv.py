# Functional programming is widely applicable in the data science domain as 
# higher-order functions can be used to process data files efficiently. 
# One of the most common formats for a data file is a CSV file 
# (comma-separated value).

import csv
from collections import namedtuple
from functools import reduce

# Code for Checkpoint 1 goes here.
tree = namedtuple("tree", ["index","width","height","volume"])

with open('trees.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader)
  # Create an iterator called mapper that will “map” the records to tuples of 
  # type tree.
  # Note: the index and height are of type int; the width and volume are of 
  # type float.
  mapper = \
  map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)
  
  trees = tuple(mapper)
  print(trees)