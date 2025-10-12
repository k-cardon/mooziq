#task 3, Get Top Tracks By An Artist

import json
from task_1_artists import show_artists

def get_user_choice():
    artists = show_artists()
    
    selected_artist = input('Please input the name of an artist: ')
    
    for artist in artists:
        if artist['name'] == selected_artist.capitalize():
            artist_id = artist["id"]

    with open(f'./dataset/top_tracks/{artist_id}.json', 'r') as file:
        all_tracks = json.load(file)
    
    return all_tracks
        
def show_top_tracks():

    chosen_artist = get_user_choice()

    print(f'listing top tracks for {chosen_artist["tracks"]["artists"]["name"]}...')
    
    for track in chosen_artist['tracks']:
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

show_top_tracks()
