import os
import json
from datetime import datetime
from task_1_artists import get_all_artists, show_artists

def suffix(number):
    if 10 <= number % 100 <= 20:
        return f"{number}th"
    last_digit = number % 10
    suffix_map = {1: "st", 2: "nd", 3: "rd"}
    return f"{number}{suffix_map.get(last_digit, 'th')}"

def convert_to_date(date_string, release_precision):
    format = {"day": "%Y-%m-%d", "month": "%Y-%m", "year": "%Y"}.get(release_precision)
    try:
        return datetime.strptime(date_string, format)
    except Exception:
        return None

def get_all_albums():
    albums = {}
    folder = "./dataset/albums"
    filenames = sorted(os.listdir(folder))
    for current_album in filenames:
        if current_album.endswith(".json"):
            filepath = os.path.join(folder, current_album)
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                for album_item in data.get("items", []):
                    album_id = album_item.get("id")
                    if album_id:
                        albums[album_id] = album_item
    return albums

def get_album_artists(album):
    artist_names = []
    for album_artist in album.get("artists", []):
        artist_names.append(album_artist.get("name", ""))
    return artist_names

def format_album_date(album):
    date_string = album["release_date"]
    release_precision = album.get("release_date_precision", "day")
    album_date = convert_to_date(date_string, release_precision)
    if album_date:
        if release_precision == "year":
            return album_date.strftime("%Y")
        elif release_precision == "month":
            return album_date.strftime("%B %Y")
        else:
            return f"{album_date.strftime('%B')} {suffix(album_date.day)} {album_date.year}"
    else:
        return date_string

def sort_albums_by_date(albums_list):
    albums_list.sort(key=lambda album: convert_to_date(album["release_date"], 
    album.get("release_date_precision", "day")), reverse=True)
    return albums_list

def artist_by_name(artist_name):
    all_artists = get_all_artists()
    for artist in all_artists.values():
        if artist.get("name", "").lower() == artist_name.lower():
            return artist
    return None

def albums_by_artist_id(artist_id):
    all_albums = get_all_albums()
    artist_albums = []
    for album in all_albums.values():
        album_artist_ids = [a.get("id", "") for a in album.get("artists", [])]
        if artist_id in album_artist_ids:
            artist_albums.append(album)
    return artist_albums

def display_albums(artist_name, albums):
    if not albums:
        print(f"\nNo albums found for {artist_name}.")
        return
    sorted_albums = sort_albums_by_date(albums)
    print(f"\nListing all available albums from {artist_name.capitalize()}...:")
    for album in sorted_albums:
        formatted_date = format_album_date(album)
        print(f'- "{album["name"]}" was released in {formatted_date}.')

def show_albums(artist_name):
    artist = artist_by_name(artist_name)
    if not artist:
        print(f"No artist named '{artist_name}'")
        return
    artist_id = artist.get("id")
    albums = albums_by_artist_id(artist_id)
    display_albums(artist_name, albums)

def album_by_artist():
    show_artists()
    name = input("Enter artist name: ").strip()
    show_albums(name)
