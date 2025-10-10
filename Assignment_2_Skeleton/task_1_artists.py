# This is where the entry point of your solution should be

#task 1 

import json
import os

def get_all_artists():
    #TODO: consider making artists a dictionary with key ID instead of a list
    #TODO: sort the files by name before processing them. You are allowed to use the Python functions sorted() or .sort() for this task.
    
    artists = []
    folder = "dataset/artists"

    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                artist = json.load(file)
                artists.append(artist)
    
    return artists

#TODO: make this a function
all_artists = get_all_artists()

print(f"Artists found in the database: ")

for artist in all_artists:
    print(f"- {artist['name']}")