from reverse_geocoder import ReverseGeocoder
from read_csv import CSVReader
import requests

reader = CSVReader('input/stores.csv')
df = reader.read_csv()
df_filtered = df.where(df['country'] == 'MX').dropna()
print(df_filtered.count())

column_names = ['display_name', 'road', 'house_number', 'city', 'state', 'suburb', 'postcode', 'category', 'type', 'osm_type', 'osm_id']

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
    
    # get the address components using the ReverseGeocoder class and append the information to the dataframe
    for column_name in column_names:
        df_filtered.at[index, column_name] = address_components.get(column_name)

loader = CSVReader.save_csv('output/updated_stores_mx.csv', df_filtered, 'output/updated_stores_mx.csv')


