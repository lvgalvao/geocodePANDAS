from reverse_geocoder_geojson import ReverseGeocoder
from read_csv import CSVReader

reader = CSVReader('input/stores.csv')
df = reader.read_csv()
df_filtered = df.where(df['country'] == 'CL').dropna()

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

for index, row in df_filtered.iterrows():
    # get the latitude and longitude values from the DataFrame
    print(index)
    lat = row['latitude']
    lon = row['longitude']

    geocoder = ReverseGeocoder(lat, lon)
    
    # get the address components using the ReverseGeocoder class
    # {'category': category, 'type': type, 'display_name': display_name, 'road': road, 'house_number': house_number, 'suburb': suburb, 'city': city, 'state': state, 'postcode': postcode}
    address_components = geocoder.get_address()
    display_name = address_components.get('display_name')
    category = address_components.get('category')
    type = address_components.get('type')
    road = address_components.get('road')
    house_number = address_components.get('house_number')
    city = address_components.get('city')
    state = address_components.get('state')
    suburb = address_components.get('suburb')
    postcode = address_components.get('postcode')

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

# assign the address components lists to new columns in the DataFrame
df_filtered['display_name'] = displayed_names
df_filtered['category'] = categories
df_filtered['type'] = types
df_filtered['road'] = roades
df_filtered['house_number'] = houses_number
df_filtered['city'] = cities
df_filtered['state'] = states
df_filtered['suburb'] = suburbes
df_filtered['postcode'] = postcodes

# print the updated DataFrame

loader = CSVReader.save_csv('output/updated_stores_cl_v2.csv', df_filtered, 'output/updated_stores_cl_v2.csv')


print(df_filtered)