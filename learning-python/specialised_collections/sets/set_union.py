song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# When working with set or frozenset container, one of the most common operations we can perform is a merge. 
# To do this, we can return the union of two sets using the .union() method or | operator. 
# Doing so will return a new set or frozenset containing all elements from both sets without duplicates.

prepare_to_py = {'rock', 'heavy metal'}
py_and_dry = frozenset({'classic', 'rock'})
# Get the union using the .union() method
combined_tags = prepare_to_py.union(py_and_dry)
# Using |:
frozen_combined_tags = py_and_dry | prepare_to_py

# ---

# First, create an empty dictionary called new_song_data which will hold the merged tag data.
new_song_data = dict()

# Our goal now is to consolidate the tags into one dictionary for each category.
# Loop over song_data.items() (all the items in song_data)
# On each iteration of the loop, create a set for each category of tags. This will require creating two new sets, one for song_data and one for user_tag_data.
# In addition to creating the sets on each iteration, create a new key inside of new_song_data for each category and set the value to be a union of the two new sets.
for key, value in song_data.items():
  song_tag_set = set(value)
  user_tag_set = set(user_tag_data[key])
  new_song_data[key] = song_tag_set | user_tag_set 

print(new_song_data)



