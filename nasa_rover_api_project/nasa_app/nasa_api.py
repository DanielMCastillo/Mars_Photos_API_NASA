import requests

NASA_API_KEY ="YOUR_API_KEY_HERE"
BASE_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

def get_mars_photos(earth_date='2020-07-01'):
    params = {
        'earth_date': earth_date,
        'api_key': NASA_API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get('photos', [])
    else:
        return []