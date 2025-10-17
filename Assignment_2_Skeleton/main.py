from top_tracks import show_top_tracks
from task_1_artists import show_artists
from song_creativity import analyze_song_lyrics
from lyrics_search import search_lyrics
# from longest_sequence import find_longest_sequence
from task_2 import album_by_artist
from task_5 import list_album_year
from task_4_export_art_data import export_artists

#add all our files to a folder, then import all the files in a single line with wildcard?
#reorganize the functions to that they are importing json in the same file, for example, to prevent repeeat imports

def main():
    menu = """
    1. Get All Artists
    2. Get All Albums By An Artist
    3. Get Top Tracks By An Artist
    4. Export Artist Data
    5. Get Released Albums By Year
    6. Analyze Song Lyrics
    7. Calculate Longest Unique Word Sequence In A Song
    8. Weather Forecast For Upcoming Concerts
    9. Search Song By Lyrics
    10. Exit 
    """
    selection = ''
    print('Welcome to Mooziq!\nChoose one of the options bellow:')
    while selection != '10':   
        print(menu)
        selection = input('Type your option: ')

        match selection:
            case '1':
                show_artists()
            case '2':
                album_by_artist()
            case '3':
                show_top_tracks()
            case '4':
                export_artists()
            case '5':
                list_album_year()
            case '6':
                analyze_song_lyrics()
            case '7':
                print('task 7')
                # find_longest_sequence()
            case '8':
                print('Weather Forecast For Upcoming Concerts')
            case '9':
                search_lyrics()
            case '10':
                print('Thank you for using Mooziq! Have a nice day :)')
            case _:
                print('Invalid Option')

if __name__ == "__main__":
    main()

