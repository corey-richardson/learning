# In Python, set and frozenset items cannot be accessed by a specific index. 
# This is due to the fact that both containers are unordered and have no 
# indices. However, like most other Python containers, we can use the in 
# keyword to test if an element is in a set or frozenset.

allowed_tags = \
    ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', \
    'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', \
    'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', \
    'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', \
    'romance', 'chill', 'swing']

song_data_users = \
    {'Retro Words': \
    ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', \
        'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# To start, store the tag data from song_data_users into a set called tag_set.
tag_set = set(song_data_users["Retro Words"])

# Create a list called bad_tags. 
# Then, iterate through each element of tag_set, adding tags to bad_tags that 
# don’t belong.
bad_tags = []
for tag in tag_set:
  if tag not in allowed_tags:
    bad_tags.append(tag)

# Using the collected bad_tags, write another loop to iterate over each of the
# tags in bad_tags, and remove the elements from tag_set so we have only the 
# allowed tags.
for tag in bad_tags:
  if tag in tag_set:
    tag_set.remove(tag)

song_data_users = {"Retro Words": tag_set}
print(song_data_users)