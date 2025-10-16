from task_2 import get_all_albums, convert_to_date, get_album_artists, format_album_date


def sort_albums_by_name(albums_list):
    albums_list.sort(key=lambda album: album["name"])
    return albums_list


def enter_year():
    try:
        year = int(input("Please enter a year: ").strip())
        return year
    except ValueError:
        print("Invalid year.")
        return None


def filter_album(all_albums, year):
    albums = []

    for album in all_albums.values():
        release_date = album.get("release_date")
        release_precision = album.get("release_date_precision", "day")
        album_date = convert_to_date(release_date, release_precision)
        if album_date and album_date.year == year:
            albums.append(album)

    return albums


def display_album_year(albums, year):
    print(f"\nAlbums released in the year {year}:")
    for album in albums:
        artist_names = get_album_artists(album)
        print(f'- "{album["name"]}" by {", ".join(artist_names)}')


def list_album_year():
    year = enter_year()
    if year is None:
        return

    all_albums = get_all_albums()
    albums = filter_album(all_albums, year)
    albums = sort_albums_by_name(albums)
    display_album_year(albums, year)


list_album_year()
