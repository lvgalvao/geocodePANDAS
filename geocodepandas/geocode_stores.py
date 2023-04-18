import pandas as pd
import requests
from reverse_geocoder import ReverseGeocoder
from read_csv import CSVReader

def process_stores(file):
    reader = CSVReader(file)
    df_filtered = reader.process_csv()
    df_filtered = df_filtered[df_filtered['lat'].notnull()]

    column_names = [
        "display_name",
        "road",
        "house_number",
        "city",
        "state",
        "suburb",
        "postcode",
        "category",
        "type",
        "osm_type",
        "osm_id",
    ]


    # Encontrar o índice da primeira linha com 'display_name' nulo
    start_index = df_filtered.iloc[:, 0].isnull().idxmin()

    for index in range(start_index, len(df_filtered)):
        print(index)
        if not pd.isnull(df_filtered.at[index, 'display_name']):
            continue

        lat = df_filtered.at[index, 'lat']
        lon = df_filtered.at[index, 'lon']

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

    reader.save_csv(df_filtered, file)