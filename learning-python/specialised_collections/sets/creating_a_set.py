genre_results = \
['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 
 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock',
 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 
 'classical', 'country', 'pop', 'rap', 'latin']

# In Python, there are multiple ways to create a set. A set object can be 
# created by passing an iterable object into its constructor, using curly 
# braces, or using a set comprehension.

# Creating a set with curly braces
music_genres = \
{'country', 'punk', 'rap', 'techno', 'pop', 'latin'}
# Creating a set from a list using set()
music_genres_2 = \
set(['country', 'punk', 'rap', 'techno', 'pop', 'latin'])

# A set from a list with duplicates produces a set with the duplicates 
# removed. Here is an example:
# Creating a set from a list that contains duplicates
music_genres_3 = \
set(['country', 'punk', 'rap', 'pop', 'pop', 'pop'])
# --> {'country', 'punk', 'pop', 'rap'}

# Sets can contain any combination of data types as long as they are unique 
# values.
music_different = \
{70, 'music times', 'categories', True , 'country', 45.7}

# Creating an empty set using the set() constructor
# Doing set = {} will define a dictionary rather than a set.  
empty_genres = set()

# We can create sets using a set comprehension and a data set (such as a list).
items = ['country', 'punk', 'rap', 'techno', 'pop', 'latin']
music_genres = {category for category in items if category[0] == 'p'}
# --> {'punk', 'pop'}

# ---

#  For the first step, find all of the genres of music that the users submitted
# without duplicates by creating a set from genre_results.
# Store the set in a variable called survey_genres. Finally, print survey_genres
# to see the new set!
survey_genres = {genre for genre in genre_results}
print(survey_genres)

# For this step, use a set comprehension to create a new set called 
# survey_abbreviated which stores the first three letters of each genre found
# in the survey results without duplication.
# survey_abbreviated = {genre[0]+genre[1]+genre[2] for genre in genre_results}
survey_abbreviated = {genre[0:3] for genre in genre_results}
print(survey_abbreviated)

