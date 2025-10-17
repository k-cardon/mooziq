import csv
from datetime import datetime
from task_1_artists import show_artists
from task_2 import suffix, artist_by_name


def read_weather():
    weather_file = "./dataset/weather/weather.csv"
    weather = {}
    with open(weather_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                key = (row['city_code'], datetime.strptime(
                    row['date'], "%Y-%m-%d").date())
                weather[key] = {
                    'city_name': row['city'],
                    'min_temp': float(row['temperature_min']),
                    'precipitation': float(row['precipitation']),
                    'wind_speed': float(row['wind_speed'])
                }
            except Exception:
                continue
    return weather


def read_concerts():
    concerts_file = "./dataset/concerts/concerts.csv"
    concerts = []
    with open(concerts_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                date_obj = datetime(int(row['year']), int(
                    row['month']), int(row['day']))
                concerts.append({
                    'artist': row['artist'],
                    'city_code': row['city_code'],
                    'date': date_obj
                })
            except Exception:
                continue
    return concerts


def get_weather_recommendation(min_temp, precipitation, wind_speed):
    recommendation = []
    try:
        if min_temp <= 10:
            recommendation.append("Wear warm clothes")
        if precipitation >= 2.3:
            recommendation.append("Bring an umbrella" if wind_speed <
                        15 else "Bring a raincoat")
        if min_temp > 10 and precipitation < 2.3:
            recommendation.append("Perfect weather")
    except Exception:
        recommendation.append("Weather data not available")
    return ". ".join(recommendation) + "."


def filter_artist_concerts(concerts, artist_id):
    result = []
    for concert in concerts:
        try:
            if artist_id and concert['artist'].lower() == artist_id['name'].lower():
                result.append(concert)
        except Exception:
            continue
    return result


def format_concert_output(concert, weather_data):
    key = (concert['city_code'], concert['date'].date())
    weather = weather_data.get(key)
    try:
        if weather:
            recommendation = get_weather_recommendation(
                weather['min_temp'], weather['precipitation'], weather['wind_speed'])
            city_name = weather['city_name']
        else:
            recommendation = "Weather data not available."
            city_name = concert['city_code']
    except Exception:
        recommendation = "Weather data not available."
        city_name = concert['city_code']
    return f"- {city_name}, {concert['date'].strftime('%B')} {suffix(concert['date'].day)} {concert['date'].year}. {recommendation}"


def print_concert_forecast(artist, concerts, weather_data):
    selected_concerts = filter_artist_concerts(concerts, artist)
    if not selected_concerts:
        print("No upcoming concerts for this artist.")
        return

    print(f"Fetching weather forecast for '{artist['name']}' concerts...")
    print(f"{artist['name']} has {len(selected_concerts)} upcoming concerts:")

    for concert in sorted(selected_concerts, key=lambda x: x['date']):
        print(format_concert_output(concert, weather_data))


def forecast_upcoming_concerts():
    try:
        weather_data = read_weather()
        concerts = read_concerts()
        show_artists()
        artist_name = input(
            "Please input the name of one of the following artists: ").strip()
        artist = artist_by_name(artist_name)
        if not artist:
            print("Artist not found.")
            return
        print_concert_forecast(artist, concerts, weather_data)
    except Exception:
        print("Error while fetching concert forecast.")
