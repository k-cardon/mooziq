#task 9, Search Song by Lyrics

from song_creativity import get_songs_with_lyrics
import re
import json
import os

def create_lyrics_index():
    songs = get_songs_with_lyrics()
    normalized_songs = []
    inverted_index = {}

    #TODO: update when Piyanon finishes task 7
    pattern = r"[!,.?()';:\-\"]"

    for song in songs:
        normalized_song_1 = song['lyrics'].lower().replace('\n', ' ')
        normalized_song_2 = re.sub(pattern, '', normalized_song_1)
        song['new_song'] = normalized_song_2
        normalized_songs.append(song)
    
    for song in normalized_songs:
        for word in song['new_song'].split():
            if word not in inverted_index:
                inverted_index[word] = [song['title']]
            elif word in inverted_index and song['title'] not in inverted_index[word]:
                inverted_index[word].append(song['title'])

    with open ('./dataset/inverted_index.json', 'w') as file:
        json.dump(inverted_index, file)

def search_lyrics():

    #create file, if file does not yet exist
    if not os.path.isfile('./dataset/inverted_index.json'):
        create_lyrics_index()
    
    lyrics = input('What do you want to search?: ')
    split_lyrics = lyrics.lower().split()
    found_matches = {}

    with open ('./dataset/inverted_index.json', 'r') as file: 
        inverted_index = json.load(file)

    for lyric in split_lyrics: 
        if lyric in inverted_index:
            for song in inverted_index[lyric]:
                if song not in found_matches:
                    found_matches[song] = 1
                else:
                    found_matches[song] += 1
                    
    print("Listing matches for {lyrics}'...")
    for song, matches in found_matches.items():
        print(f"- {song} with a score of {matches}")    
