site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = \
    ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', \
    'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', \
    'camisole top', 'sweatshirt']

# When we try to access a key-value pair in a dictionary, but the key does not 
# exist, a dictionary will normally throw a KeyError.
# In certain cases, it might be better to avoid throwing an error. 
# One of the ways Python offers to deal with this issue is by having a default
# missing value in the dictionary, and this is exactly what the defaultdict 
# collection does.

# from collections import defaultdict
# validate_prices = defaultdict(lambda: 'No Price Assigned')
# # Next, we can set the keys and values like a regular dict:
# validate_prices['jeans'] = 19.99
# validate_prices['shoes'] = 24.99
# validate_prices['t-shirt'] = 9.99
# validate_prices['blouse'] = 19.99
# # Finally, we access an invalid key to observe the result:
# print(validate_prices['jacket'])
# # Would output:
# # No Price Assigned

# For this first checkpoint, import the defaultdict class from the collections
# module and create a new variable called validated_locations. 
# Use the defaultdict constructor to create a new defaultdict object in 
# validated_locations which defaults missing keys to have a value of 
# 'TODO: Add to website'.
from collections import defaultdict
validated_locations = defaultdict(lambda: "TODO: Add to website")

# Not only can we create a defaultdict from scratch, but we can also create one
# from an existing dictionary. To do this, we can use the .update() method from
# the defaultdict class. This behaves the same way as the .update() method from
# the dict class.
# Use the .update() method to move all of the site_location data into 
# validated_locations.
validated_locations.update(site_locations)

# Iterate through every item in the updated_products list and update the 
# site_locations dictionary with the values from validated_locations.
for item in updated_products:
  site_locations[item] = validated_locations[item]

print(site_locations)