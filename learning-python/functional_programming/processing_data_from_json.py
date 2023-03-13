import json
from collections import namedtuple
from functools import reduce

city = namedtuple(
    "city", [
        "name", 
        "country", 
        "coordinates", 
        "continent"] )

with open('cities.json') as json_file:
  data = json.load(json_file) 

cities = map(lambda x: 
    city(
        x["name"], 
        x["country"], 
        x["coordinates"], 
        x["continent"]),
    data["city"])

# Store all cities that are on the continent of Asia in the tuple called asia.
asia = tuple( filter(lambda x: x[3] == "Asia", cities) )
print(asia)

# Find the western-most city in the asia tuple and store it in the west 
# variable.
west = reduce(lambda x,y: x if x < y else y, asia)

print(west)