#task 3, Get Top Tracks By An Artist

import json
from task_1_artists import get_all_artists, show_artists

def get_user_choice():
    artist_id = ''

    artists = get_all_artists()

    show_artists()
    
    selected_artist = input('Please input the name of an artist: ')
    
    
    for item_id, info in artists.items():
        if info['name'].lower() == selected_artist.lower():
            artist_id = item_id
    
    try:
        with open(f'./dataset/top_tracks/{artist_id}.json', 'r', encoding="utf-8") as file:
            all_tracks = json.load(file)
    except:
        return
            
    return all_tracks
        
def show_top_tracks():
    selection = get_user_choice()

    if selection == None:
        print('Artist not found.')

    else:
        artist = selection['tracks'][0]['album']['artists'][0]['name']

        print(f'listing top tracks for {artist}...')
        
        for track in selection['tracks']:
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
