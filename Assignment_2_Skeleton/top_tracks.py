#task 3, Get Top Tracks By An Artist

import os
import json
from task_1_artists import get_all_artists

#TODO: refactor because this is redundant from song_creativity.py?
def get_top_tracks():
    contents = os.listdir('./dataset/top_tracks')

    top_tracks = []

    for i in range(len(contents)):
        artist_id = contents[i]
        with open(f'./dataset/top_tracks/{artist_id}', 'r') as file:
            tracklist = json.load(file)
            top_tracks.append(tracklist)
    
    return top_tracks


def get_user_choice():
    artists = get_all_artists()
    all_top_tracks = get_top_tracks()
    
    #TODO: consider making this another function in Piyanont's file?
    print('Artists found in the database:')
    for artist in artists:
        print(f"- {artist['name']}")

    selected_artist = input('Please input the name of an artist: ')
    
    for artist in artists:
        if artist['name'] == selected_artist.capitalize():
            artist_id = artist["id"]

    print(f'listing top tracks for {selected_artist}...')

    # TODO: implement json parsing of ./dataset/top_tracks
    with open(f'./dataset/top_tracks/{artist_id}.json', 'r') as file:
        all_tracks = json.load(file)
        
    for track in all_tracks['tracks']:
        name = track['name']
        popularity_rank = track['popularity']
        if popularity_rank <= 30:
            popularity_message = 'No one knows this song.'
        elif popularity_rank <= 50:
            popularity_message = 'Popular song.'
        elif popularity_rank <= 70:
            popularity_message = 'It is quite popular now!'
        else:
            popularity_message = 'It is made for the charts!'


        print(f'- \"{name}\" has a popularity score of {popularity_rank}. {popularity_message}')

