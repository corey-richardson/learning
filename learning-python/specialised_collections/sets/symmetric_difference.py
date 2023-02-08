# We can think of this operation as the opposite of the intersection operation.
# A resulting set will include all elements from the sets which are in one or 
# the other, but not both.

# (A n B)'

# Find the elements which are exclusive to each song and not shared using the method
# exclusive_tags = prepare_to_py.symmetric_difference(py_and_dry)
# print(exclusive_tags)

# Find the elements which are exclusive to each song and not shared using the operator
# frozen_exclusive_tags = py_and_dry ^ prepare_to_py
# print(frozen_exclusive_tags)

user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# The users of our app would like to be able to see which tags are unique 
# between them and their friends.
# In order to find this, we can use the symmetric difference.
# First, create a set called user_tags.
# Use a loop to populate the set to contain all of the tags from the songs in 
# user_song_history.
user_tags = set()
for song, tags in user_song_history.items():
  for tag in tags:
    user_tags.add(tag)

# Next, repeat the same logic in order to collect all of the tags from the 
# friend_song_history and store it in a set called friend_tags.
friend_tags = set()
for song, tags in friend_song_history.items():
  for tag in tags:
    friend_tags.add(tag)

# Finally, find the unique tags by getting the symmetric difference between
# user_tags and friend_tags.
unique_tags = user_tags ^ friend_tags
print(unique_tags)