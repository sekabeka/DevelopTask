import requests
from datetime import datetime
headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://open-meteo.com',
    'Referer': 'https://open-meteo.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

def get_coordinates(city: str):
    params = {
        'name': city,
        'count': '1',
        'language': 'ru',
        'format': 'json',
    }
    response = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=params, headers=headers)
    data = response.json()
    result = data['results'][0]
    lat, lon = result['latitude'], result['longitude']
    return (lat, lon)

def get_forecast_weather(city):
    lat, lon = get_coordinates(city)
    params = {
        'latitude': str(lat),
        'longitude': str(lon),
        'hourly': 'temperature_2m',
        'format': 'json',
        'timeformat': 'unixtime',
    }
    response = requests.get('https://api.open-meteo.com/v1/forecast', params=params, headers=headers)
    data = response.json()
    result = []
    for stamp, t in zip(data['hourly']['time'], data['hourly']['temperature_2m']):
        stamp = datetime.fromtimestamp(stamp)
        result.append({
            'temp' : t,
            'datetime' : str(stamp)
        })
    return result
