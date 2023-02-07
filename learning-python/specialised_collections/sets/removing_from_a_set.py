# There are two methods for removing specific elements from a set:
# The .remove() method searches for an element within the set and removes it 
# if it exists, otherwise, a KeyError is thrown.
# The .discard() method works the same way but does not throw an exception if 
# an element is not present.

# Note that items cannot be removed from a frozenset so neither of these 
# methods would work.

song_data_users = \
    {'Retro Words': \
        ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# To start off, we need another set for the tag data within song_data_users. 
# Create a set called tag_set and store the tag data for 'Retro Words'.
tag_set = set( song_data_users["Retro Words"] )

# Now we need to remove the tags which are unrelated to music. 
# In this case, remove the tags: 'onion', 'helloworld', and 'spam'.
tag_set.remove("onion")
tag_set.remove("helloworld")
# tag_set.discard("vegemite") # would throw an error
tag_set.discard("spam")
tag_set.discard("vegemite") # wont throw an error

# For the last step, replace the value of the key, 'Retro Words' inside of 
# song_data_users so that it is equal to the updated tag set.
song_data_users = {"Retro Words": tag_set}
print(song_data_users)