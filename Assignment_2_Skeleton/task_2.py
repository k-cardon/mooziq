import os
import json
from datetime import datetime
from task_1_artists import get_all_artists, show_artists


def suffix(n):
    if 10 <= n % 100 <= 20:
        return f"{n}th"
    last_digit = n % 10
    suffix_map = {1: "st", 2: "nd", 3: "rd"}
    return f"{n}{suffix_map.get(last_digit, 'th')}"


def parse_date(date_str, precision):
    fmt = {"day": "%Y-%m-%d", "month": "%Y-%m", "year": "%Y"}.get(precision)
    try:
        return datetime.strptime(date_str, fmt)
    except Exception:
        return None


def get_all_albums():
    albums = {}
    folder = "./dataset/albums"
    filenames = sorted(os.listdir(folder))

    for filename in filenames:
        if filename.endswith(".json"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data.get("items", []):
                    album_id = item.get("id")
                    if album_id:
                        albums[album_id] = item
    return albums


def show_albums(artist_name):
    all_artists = get_all_artists()

    artist = next(
        (a for a in all_artists.values() if a.get("name", "").lower() == artist_name.lower()),
        None
    )
    if not artist:
        print(f"No artist named '{artist_name}'")
        return

    artist_id = artist.get("id")
    all_albums = get_all_albums()
    artist_albums = {
        a_id: a for a_id, a in all_albums.items()
        if any(ar.get("id") == artist_id for ar in a.get("artists", []))
    }

    if not artist_albums:
        print(f"No albums found for {artist_name}")
        return

    sorted_albums = sorted(
        artist_albums.values(),
        key=lambda x: parse_date(x["release_date"], x.get("release_date_precision", "day")) or datetime.min,
        reverse=True,
    )

    print(f"\nAlbums by {artist_name}:")
    for album in sorted_albums:
        date_obj = parse_date(album["release_date"], album.get("release_date_precision", "day"))
        if date_obj:
            p = album.get("release_date_precision", "day")
            formatted_date = (
                date_obj.strftime("%Y") if p == "year"
                else date_obj.strftime("%B %Y") if p == "month"
                else f"{date_obj.strftime('%B')} {suffix(date_obj.day)} {date_obj.year}"
            )
        else:
            formatted_date = album["release_date"]
        print(f'- "{album["name"]}" released on {formatted_date}')


def album_by_artist():
    show_artists()
    name = input("\nEnter artist name: ").strip()
    show_albums(name)


album_by_artist()
