from reverse_geocoder import ReverseGeocoder
from read_csv import CSVReader

reader = CSVReader('input/stores.csv')
df = reader.read_csv()
df_filtered = df.where(df['country'] == 'CO').dropna()

# create empty lists to store the address components
addresses = []

for index, row in df_filtered.iterrows():
    # get the latitude and longitude values from the DataFrame
    lat = row['latitude']
    lon = row['longitude']

    geocoder = ReverseGeocoder(lat, lon)

    # get the address components using the ReverseGeocoder class
    address_components = geocoder.get_address()
    address = address_components['address']

    # append the address components to the lists
    addresses.append(address)

# assign the address components lists to new columns in the DataFrame
df_filtered['address'] = addresses

# print the updated DataFrame

loader = CSVReader.save_csv('output/updated_stores_co.csv', df_filtered, 'output/updated_stores_co.csv')


print(df_filtered)