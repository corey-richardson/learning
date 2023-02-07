song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Let’s say that we have two or more sets, and we want to find which items both sets have in common. The set container has a method called .intersection() which returns a new set or frozenset consisting of those elements.

# frozen_intersected_tags = py_and_dry.intersection(prepare_to_py)
# intersected_tags = prepare_to_py & py_and_dry

# ---

# First, create a variable called tags_int that stores the intersection between the tags for the user_recent_songs two recent songs 'Retro Words' and 'Lowkey Space'. Remember to convert each list into a set to perform the operation.
# We will be using these common tags as a basis for finding a recommended song in song_data.
# Remember to pass the tags from each recent song into the set() constructor.

tags_int = set(song_data["Retro Words"]) & set(song_data["Lowkey Space"])

# Find all other songs in song_data which have these tags. Store the songs which have any matching tags into a dictionary called recommended_songs.
recommended_songs = {}
for key, song in song_data.items():
  for tag in song:
    if tag in tags_int:
      if key not in user_recent_songs:
        recommended_songs[key] = song
print(recommended_songs)
# recommended_songs = (song for song in shared_tag if song not in user_recent_songs)

# <loop through each song in song_data> 
#   <loop through each tag in song_data for a specific song>
#    < if the tag is inside of of the specific song> 
#      < if the user has not listened to the specific song> 
#         <Add the song and associated tags to recommended_songs>



