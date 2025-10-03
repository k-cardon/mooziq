def get_top_tracks():
    
    artists = get_all_artists()
    print(artists)

    selected_artist = input('Please input the name of an artist: ')
    print(f'Listing top tracks for {selected_artist}: ')

    tracks = []

    # TODO: implement json parsing of ./dataset/top_tracks

    for track in tracks:
        popularity_rank = track['popularity']
        if popularity_rank > 29:
            popularity_message = 'No one knows this song.'
        elif popularity_rank > 49:
            popularity_message = 'Popular song.'
        elif popularity_rank > 69:
            popularity_message = 'It is quite popular now!'
        else:
            popularity_message = 'It is made for the charts!'

        print(f'- \'{track['name']} has a popularity score of {popularity_rank}. {popularity_message}')
    