import os
import json
import csv
from task_1_artists import get_all_artists


def get_top_tracks():
    folder = './dataset/top_tracks'
    top_tracks = []
    
    for filename in sorted(os.listdir(folder)):
        if filename.endswith('.json'):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                tracklist = json.load(file)
                top_tracks.append(tracklist)

    return top_tracks

def get_album():
    folder = './dataset/albums'
    all_albums = []
    
    for filename in sorted(os.listdir(folder)):
        if filename.endswith('.json'):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                album = json.load(file)
                all_albums.append(album)

    return all_albums

def export_artists():

    show_all_artists = get_all_artists()
    all_track_lists = get_top_tracks()
    all_album = get_album()

    csv_data = []
    artists_csv = {}
    counter = 0

    csv_filepath = "./dataset/artist-data.csv"

    if not os.path.exists(csv_filepath):
        with open(csv_filepath, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["artist_id", "artist_name", "number_of_albums", "top_track_1", "top_track_2", "genres"])

    if os.path.exists(csv_filepath):
        with open(csv_filepath, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                artists_csv[counter] = row[1]
                counter += 1

    for artist_id, artist in show_all_artists.items():
            print(f"- {artist['name']}")

    input_artist = input(f"Please input the name of one of the following artists:").title()

    if input_artist in artists_csv.values():
        print(f'Exporting "{input_artist}" data to CSV file...')
        print("Data successfully updated.")

    else:
        print(f'Exporting "{input_artist}" data to CSV file...')
        print("Data successfully appended.")
        artists_csv[counter] = input_artist
        counter += 1

        for track_data in get_top_tracks():
            tracks = track_data.get("tracks",[])
            
            if tracks:
                if input_artist == tracks[0]["artists"][0]["name"]:

                    artist_name = tracks[0]["artists"][0]["name"]

                    artist_id = tracks[0]["artists"][0]["id"]
                    
                    album_count = 0
                    for album_file in get_album():
                        items = album_file.get("items", [])
                        if not items:
                            continue 
                        artists = items[0].get("artists", [])
                        if any(artist.get("id") == artist_id for artist in artists):
                            album_count += len(items)

                    top_2 = tracks[:2]
                    top_track_1 = top_2[0]["name"]
                    top_track_2 = top_2[1]["name"]
                    
                    genres = ""
                    if artist_id in show_all_artists:
                        genres_list = show_all_artists[artist_id]["genres"]
                        if genres_list:
                            genres = ", ".join(genres_list)
                    
                    csv_data.append([artist_id, artist_name, album_count, top_track_1, top_track_2, genres])
        
                    with open(csv_filepath, 'a', encoding='utf-8', newline='') as file:
                        writer = csv.writer(file)
                        if file.tell() == 0:
                            writer.writerow(['artist_id', 'artist_name', 'number_of_albums', 'top_track_1', 'top_track_2', 'genres'])
                        writer.writerows(csv_data)     

