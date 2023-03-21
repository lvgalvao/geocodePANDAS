from reverse_geocoder_geojson import ReverseGeocoder
from read_csv import CSVReader
import requests

reader = CSVReader('input/stores.csv')
df = reader.read_csv()
df_filtered = df.where(df['country'] == 'MX').dropna()
print(df_filtered.count())

# create empty lists to store the address components
displayed_names = []
roades = []
categories = []
types = []
houses_number = []
cities = []
states = []
suburbes = []
postcodes = []
osm_types = []
osm_ides = []
openstreetmap_urles = []

failed_indices = []


for index, row in df_filtered.iterrows():
    # get the latitude and longitude values from the DataFrame
    print(index)
    lat = row['latitude']
    lon = row['longitude']

    geocoder = ReverseGeocoder(lat, lon)

    try:
        address_components = geocoder.get_address()
    except requests.exceptions.RequestException as e:
        if "Connection reset by peer" in str(e):
            print(f"Error at index {index}: {e} (Connection reset by peer)")
        else:
            print(f"Error at index {index}: {e}")
        break
    
    # get the address components using the ReverseGeocoder class
    # {'category': category, 'type': type, 'display_name': display_name, 'road': road, 'house_number': house_number, 'suburb': suburb, 'city': city, 'state': state, 'postcode': postcode}
    display_name = address_components.get('display_name')
    road = address_components.get('road')
    house_number = address_components.get('house_number')
    city = address_components.get('city')
    state = address_components.get('state')
    suburb = address_components.get('suburb')
    postcode = address_components.get('postcode')
    category = address_components.get('category')
    type = address_components.get('type')
    osm_type = address_components.get('osm_type')
    osm_id = address_components.get('osm_id')

    # append the address components to the lists
    displayed_names.append(display_name)
    categories.append(category)
    types.append(type)
    roades.append(road)
    houses_number.append(house_number)
    cities.append(city)
    states.append(state)
    suburbes.append(suburb)
    postcodes.append(postcode)
    osm_types.append(osm_type)
    osm_ides.append(osm_id)
    openstreetmap_urles.append(f'https://www.openstreetmap.org/{osm_type}/{osm_id}')

# assign the address components lists to new columns in the DataFrame
df_filtered['display_name'] = displayed_names
df_filtered['road'] = roades
df_filtered['house_number'] = houses_number
df_filtered['city'] = cities
df_filtered['state'] = states
df_filtered['suburb'] = suburbes
df_filtered['postcode'] = postcodes
df_filtered['category'] = categories
df_filtered['type'] = types
df_filtered['osm_type'] = osm_types
df_filtered['osm_id'] = osm_ides
df_filtered['openstreetmap'] = openstreetmap_urles



# print the updated DataFrame

loader = CSVReader.save_csv('output/updated_stores_mx.csv', df_filtered, 'output/updated_stores_mx.csv')

if failed_indices:
    print(f"Failed to get address for the following indices: {failed_indices}")

