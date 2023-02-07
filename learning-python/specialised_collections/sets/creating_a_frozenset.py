# Unlike a normal set, you can only create a frozenset using its constructor. 
# Remember that using a frozenset means that you cannot modify the elements 
# inside of it.

# Creating a frozenset from a list
frozen_music_genres = \
    frozenset(['country', 'punk', 'rap', 'techno', 'pop', 'latin'])

# Creating an empty frozenset
empty_frozen_music_genres = frozenset()

# ---

# After calculating the results for the top music genres from the survey, your
# teammates have sent you a list containing the top three results.
top_genres = ['rap', 'rock', 'pop']

# In order to preserve this data and prevent it from being modified, create a
# frozenset called frozen_top_genres from the top_genres data. Print our 
# frozen_top_genres to see it!

frozen_top_genres = frozenset(top_genres)
print(frozen_top_genres)