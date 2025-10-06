def get_top_tracks():
    import json

    # TODO: connect to other function when its ready
    # artists = get_all_artists()
    # print(artists)

    # selected_artist = input('Please input the name of an artist: ')
    # print(f'Listing top tracks for {selected_artist}: ')

    # TODO: implement json parsing of ./dataset/top_tracks
    with open('./dataset/top_tracks/0L8ExT028jH3ddEcZwqJJ5.json', 'r') as file:
        all_tracks = json.load(file)
        
        for listing in all_tracks.values():
            for item in listing:
                # print(f'variable listing = {item}')
                # print(f'variable listing type = {type(item)}')
                name = item['name']
                popularity_rank = item['popularity']
                if popularity_rank <= 30:
                    popularity_message = 'No one knows this song.'
                elif popularity_rank <= 50:
                    popularity_message = 'Popular song.'
                elif popularity_rank <= 70:
                    popularity_message = 'It is quite popular now!'
                else:
                    popularity_message = 'It is made for the charts!'
                # print(name)
                # print(popularity_rank)

                print(f'- \'{name}\' has a popularity score of {popularity_rank}. {popularity_message}')

get_top_tracks()