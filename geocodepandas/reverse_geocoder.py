import requests

class ReverseGeocoder:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.url = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}'

    def get_address(self):
        # send a GET request to the API endpoint
        response = requests.get(self.url)

        # get the JSON data from the API response
        data = response.json()

        # get the address components
        address = data['display_name']
        city = data['address'].get('city')
        state = data['address'].get('state')
        state_district = data['address'].get('state_district')
        postcode = data['address'].get('postcode')

        return {'address': address, 'city': city, 'state': state, 'state_district': state_district, 'postcode': postcode}