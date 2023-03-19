from reverse_geocoder import ReverseGeocoder
from read_csv import CSVReader

reader = CSVReader('assets/stores.csv')
df = reader.read_csv()
print(df.head())

# set the latitude and longitude values
lat = 37.7749
lon = -122.4194

geocoder = ReverseGeocoder(lat, lon)
address_components = geocoder.get_address()
print(address_components)