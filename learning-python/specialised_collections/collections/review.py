

overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

# For the first step, import the deque and namedtuple classes from the collections module and create a new deque called split_prices.
from collections import deque, namedtuple
split_prices = deque()

# Now that the deque has been created, for every clothes item in the overstock_items list, if the price if greater than 20 dollars than append the item to the front of split_prices, otherwise append it to the back of split_prices.
for item in overstock_items:
  if item[1] >= 20:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)
print(split_prices)

# To make the data easier to read and work with, create a namedtuple subclass called ClothesBundle.
# Set the typename to ClothesBundle and the field_names to bundle_items and bundle_price.
ClothesBundle = namedtuple("ClothesBundle",["bundle_items", "bundle_price"])

# First, create an empty list called bundles. 
# Use a loop to continue iterating as long as there are at least 5 elements left in split_prices.
# On each iteration, append a new ClothesBundle object to the bundles list. 
# The ClothesBundle object will be created by making a bundle of three cheap items and two expensive items.
# This can be accomplished using list of items by popping from the back of split_prices three times and the popping from the front of split_prices two times.
# Use that list of clothes items as the bundle_items in theClothesBundle.
# Calculate the sum of the prices for the bundle and store that as the bundle_price in the ClothesBundle.
bundles = []
while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(),split_prices.popleft()]

  calc_price = sum(bun[1] for bun in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calc_price))

# Use the bundles list to find out which bundles should be promoted. 
# Create a new list called promoted_bundles. 
# For every bundle in bundles which has a total value of over 100 dollars, add that bundle to promoted_bundles.
promoted_bundles = []
for bundle in bundles:
  if bundle.bundle_price > 100:
    promoted_bundles.append(bundle)

print(promoted_bundles)
