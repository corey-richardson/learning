# Find the elements which are only in prepare_to_py
# only_in_prepare_to_py = prepare_to_py.difference(py_and_dry)

# Find the elements which are only in py_and_dry
# only_in_py_and_dry = py_and_dry - prepare_to_py

# You can use .difference_update() to update the original set with the result
# instead of returning a new set or frozenset object.

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Create a new variable called tag_diff that is the set difference between the 
# tags inside of the one song of user_liked_song and the one song of 
# user_disliked_song.
tag_diff = set(user_liked_song["Back To Art"]) - set(user_disliked_song["Retro Words"])
print(tag_diff)

# Now that you know the difference in tags between the liked song and disliked 
# song, use those tags to find any songs from song_data which contain them.
# Make sure not to include the liked and disliked songs. Store the newly found 
# songs into a dictionary called recommended_songs.

# <loop through each song in song_data> 
#  <loop through each tag in song_data for a specific song>
#   <if the tag is inside of tag_diff> 
#    <check if the user has not listened to the specific song in user_liked_song
#    or user_disliked_song> 
#         <add the song and associated tags to recommended_songs>

recommended_songs = {}
for key, song in song_data.items():
  for tag in song:
    if tag in tag_diff:
      if key not in user_liked_song and key not in user_disliked_song:
        recommended_songs[key] = song
print(recommended_songs)