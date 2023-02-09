music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# For these checkpoints, we will review the different operations which you can perform on set and frozenset containers.
# First, create a frozenset called my_tags which contains the elements: 'pop', 'electronic', 'relaxing', 'slow', and 'synth'.
my_tags = frozenset(["pop","electronic","relaxing","slow","synth"])

# Try finding the union of music_tags and my_tags, but make sure to return the result as a frozenset. Store the result in a variable called frozen_tag_union.
frozen_tag_union = frozenset(music_tags | my_tags)
# A u B

# Now store the intersection of music_tags and my_tags into a variable called regular_tag_intersect. Make sure that it is stored as a normal set this time.
regular_tag_intersect = music_tags & my_tags
# A n B

# Now try finding the difference of my_tags with music_tags. Store this result in a variable called frozen_tag_difference. The type of the result should be a frozenset.
frozen_tag_difference = frozenset(my_tags - music_tags)
# A n B'

# Finally, get the symmetric difference of music_tags with my_tags and store it in a variable called regular_tag_sd. The result should should be a set and not a frozenset.
regular_tag_sd = music_tags ^ my_tags 
# (A n B)'