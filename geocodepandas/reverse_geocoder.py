import requests

class ReverseGeocoder:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.url = f'https://nominatim.openstreetmap.org/reverse?format=geojson&lat={lat}&lon={lon}'

    def _send_request(self):
        response = requests.get(self.url)
        return response.json()

    def _parse_address(self, data):
        if 'features' in data and len(data['features']) > 0:
            properties = data['features'][0]['properties']
            address = properties['address']
            result = {
                'category': properties.get('category'),
                'type': properties.get('type'),
                'display_name': properties.get('display_name'),
                'osm_type': properties.get('osm_type'),
                'osm_id': properties.get('osm_id'),
                'road': address.get('road'),
                'house_number': address.get('house_number'),
                'suburb': address.get('suburb'),
                'city': address.get('city'),
                'state': address.get('state'),
                'postcode': address.get('postcode')
            }
        else:
            result = {
                'category': None,
                'type': None,
                'display_name': None,
                'osm_type': None,
                'osm_id': None,
                'road': None,
                'house_number': None,
                'suburb': None,
                'city': None,
                'state': None,
                'postcode': None
            }
        return result

    def get_address(self):
        data = self._send_request()
        address = self._parse_address(data)
        return address
