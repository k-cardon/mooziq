#task 6, Song Creativity Score

import os 
import json

def get_songs_with_lyrics():
    contents = os.listdir('./dataset/songs/')

    songs_with_lyrics = []

    for i in range(len(contents)):
        filename = contents[i]
        with open(f'./dataset/songs/{filename}', 'r') as file:
            song = json.load(file)
            songs_with_lyrics.append(song)
    
    return songs_with_lyrics

def analyze_song_lyrics():
    
    songs = get_songs_with_lyrics()

    print('Available songs:')
    for i in range(len(songs)):
        print(f'{i}: {songs[i]["title"]}')

    #TODO: implement lyrics analysis with regex
