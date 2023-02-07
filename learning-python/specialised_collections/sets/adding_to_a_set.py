# There are two different ways to add elements to a set:
# The .add() method can add a single element to the set.
# The .update() method can add multiple elements.

# Neither of these methods will add a duplicate item to a set.
# A frozenset can not have any items added to it and so neither of these 
# methods will work.
# Notice that when the elements are printed, they are not printed in the same 
# order in which they entered the set. This is because set and frozenset 
# containers are unordered.

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# For this version of the app, we are provided a song_data dictionary as well 
# as a few tags from users in the form of strings.
# For the first step, create a new set called tag_set from the original song’s
# tags located in song_data.
tag_set = set(song_data["Retro Words"])
print(tag_set)

# Next, add the three user tag strings to tag_set.
# tag_set.add(user_tag_1)
# tag_set.add(user_tag_2)
# tag_set.add(user_tag_3)
# OR
tag_set.update([user_tag_1, user_tag_2, user_tag_3])
print(tag_set)

# Finally, update song_data so that the value of the key, 'Retro Words' is 
# equal to the updated tag set.
song_data = {'Retro Words': tag_set}