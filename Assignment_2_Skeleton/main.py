from top_tracks import get_top_tracks

def main():
    selection = ''

    while selection != '10':
        menu = """
        Welcome to Mooziq!
        Choose one of the options below:

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
        
        print(menu)
        selection = input('Type your option: ')

        match selection:
            case '1':
                print('Get All Artists')
            case '2':
                print('Get All Albums By An Artist')
            case '3':
                get_top_tracks()
            case '4':
                print('Export Artist Data')
            case '5':
                print('Get Released Albums By Year')
            case '6':
                print('Analyze Song Lyrics')
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

