from requests import get
from dotenv import load_dotenv

load_dotenv()

api_key = input('Put your API Key here: ')
url = "https://maps.googleapis.com/maps/api/distancematrix/json"

origin = input('Where you want to start your trip? ')
destination = input('What is your destination address? ')
consumption = float(input('What is yours car fuel consumption? '))
price = float(input('What is the fuel cost? '))

payload = {
    'origins': origin,
    'destinations': destination,
    'key': api_key
}
response = get(url, payload)
body = response.json()
distance = body['rows'][0]['elements'][0]['distance']
duration = body['rows'][0]['elements'][0]['duration']

cost = price * distance['value'] / 1000 * consumption / 100
print(f'Your trip cost equals: {cost}')
