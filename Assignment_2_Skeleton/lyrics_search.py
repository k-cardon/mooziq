#task 9, Search Song by Lyrics

from song_creativity import get_songs_with_lyrics

songs = get_songs_with_lyrics()

#TODO: preprocessing for lyrics (lowercase, remove punctuation and newlines, use task 7)

#TODO: create reverse index and cache it -- save as a file in dataset

#TODO: accept user input of lyrics and search for each word separately in reverse_index.json

#TODO: the more words that match the requested lyrics, the higher the score. 

#TODO: return the score for each matched song