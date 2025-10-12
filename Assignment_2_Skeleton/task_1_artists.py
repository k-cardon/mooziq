
import json
import os

def get_all_artists():

    artists = {}

    folder = "dataset/artists"
    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
        if filename.endswith(".json"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                artist = json.load(file)
                artist_id = artist.get("id")
                if artist_id:
                    artists[artist_id] = artist
    
    return artists

def show_artists():
        
    all_artists = get_all_artists()

    print(f"Artists found in the database: ")

    for artist_id, artist in all_artists.items():
        print(f"- {artist['name']}")

if __name__ == "__main__":
    show_artists()
