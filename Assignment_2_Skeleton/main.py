from top_tracks import get_user_choice
from task_1_artists import get_all_artists
from song_creativity import analyze_song_lyrics

def main():
    menu = """Welcome to Mooziq!
    Choose one of the options bellow:

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

    while selection != '10':   
        print(menu)
        selection = input('Type your option: ')

        match selection:
            case '1':
                get_all_artists()
            case '2':
                print('Get All Albums By An Artist')
            case '3':
                get_user_choice()
            case '4':
                print('Export Artist Data')
            case '5':
                print('Get Released Albums By Year')
            case '6':
                analyze_song_lyrics()
            case '7':
                print('Calculate Longest Unique Word Sequence In A Song')
            case '8':
                print('Weather Forecast For Upcoming Concerts')
            case '9':
                print('Search Song By Lyrics')
            case '10':
                print('Thank you for using Mooziq! Have a nice day :)')
            case _:
                print('Invalid Option')

if __name__ == "__main__":
    main()

