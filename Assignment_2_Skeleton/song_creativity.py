#task 6, Song Creativity Score

import os 
import json
import re

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
    
    selection = int(input('Choose a song: '))
    chosen_song = songs[selection]['lyrics']
    title = songs[selection]['title']

    pattern_1 = r"mo"
    pattern_2 = r"\w*\?"
    pattern_3 = r"\w*!"

    new_lyrics_1 = re.sub(pattern_1, 'moo', chosen_song)
    new_lyrics_2 = re.sub(pattern_2, 'moo?', new_lyrics_1)
    new_lyrics_3 = re.sub(pattern_3, 'moo!', new_lyrics_2)

    if new_lyrics_3 == chosen_song:
        print(f'{title} is not moose-compatible!')
    else:
        with open(f'./moosified/{title} Moosified.txt', 'w', encoding='utf-8') as file:
            file.write(new_lyrics_3)
        print(f'{title} has been moos-ified!')

analyze_song_lyrics()
