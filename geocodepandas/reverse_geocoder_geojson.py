import requests

class ReverseGeocoder:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.url = f'https://nominatim.openstreetmap.org/reverse?format=geojson&lat={lat}&lon={lon}'

    def get_address(self):
        # send a GET request to the API endpoint
        response = requests.get(self.url)

        # get the JSON data from the API response
        data = response.json()

        # get the address components
        display_name = data['features'][0]['properties']['display_name']
        category = data['features'][0]['properties']['category']
        type = data['features'][0]['properties']['type']
        road = data['features'][0]['properties']['address'].get('road')
        house_number = data['features'][0]['properties']['address'].get('house_number')
        suburb = data['features'][0]['properties']['address'].get('suburb')
        city = data['features'][0]['properties']['address'].get('city')
        state = data['features'][0]['properties']['address'].get('state')
        postcode = data['features'][0]['properties']['address'].get('postcode')

        return {'category': category, 'type': type, 'display_name': display_name, 'road': road, 'house_number': house_number, 'suburb': suburb, 'city': city, 'state': state, 'postcode': postcode}