from task_2 import get_all_albums, convert_to_date, get_album_artists, format_album_date

def sort_albums_by_name(albums_list):
    albums_list.sort(key=lambda album: album["name"])
    return albums_list

def list_albums_by_year():
    year_input = input("Please enter a year: ").strip()
    if not year_input.isdigit():
        print("Invalid year.")
        return
    year = int(year_input)

    all_albums = get_all_albums()
    albums_in_year = []

    for album in all_albums.values():
        date_string = album.get("release_date")
        release_precision = album.get("release_date_precision", "day")
        album_date = convert_to_date(date_string, release_precision)
        if album_date and album_date.year == year:
            albums_in_year.append(album)

    albums_in_year = sort_albums_by_name(albums_in_year)

    print(f"\nAlbums released in the year: {year}")
    for album in albums_in_year:
        artist_names = get_album_artists(album)
        formatted_date = format_album_date(album)
        print(f'- "{album["name"]}" by {", ".join(artist_names)}')

