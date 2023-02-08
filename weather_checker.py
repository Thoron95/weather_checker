import geocoder, requests, json

g = geocoder.ip('me')

with open('config.json', mode='r') as file:
    API_KEY = json.load(file)['API_KEY']


request = f'https://api.openweathermap.org/data/2.5/weather?lat={g.lat}&lon={g.lng}&appid={API_KEY}&units=metric'
response = requests.get(request).json()

print('Here is some info about weather in your location:')
print(f'- Temperature: {round(response["main"]["temp"])}\'C')
print(f'- Feels Like: {round(response["main"]["feels_like"])}\'C')
print(f'- Humidity: {round(response["main"]["humidity"])}%')
print(f'- Weather: {response["weather"][0]["main"]}')