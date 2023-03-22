import pandas as pd
import requests
from reverse_geocoder import ReverseGeocoder
from read_csv import CSVReader

def process_stores(input_file, output_file, country_filter=None):
    reader = CSVReader(input_file)
    df = reader.process_csv()

    if country_filter:
        df_filtered = df[df["country"] == country_filter]
    else:
        df_filtered = df

    df_filtered = df_filtered[df_filtered['latitude'].notnull()]

    column_names = ['display_name', 'road', 'house_number', 'city', 'state', 'suburb', 'postcode', 'category', 'type', 'osm_type', 'osm_id']

    for index, row in df_filtered.iterrows():
        print(index)
        if not pd.isnull(row['display_name']):
            continue

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

        for column_name in column_names:
            df_filtered.at[index, column_name] = address_components.get(column_name)

    reader.save_csv(df_filtered, output_file)