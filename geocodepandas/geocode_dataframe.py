import pandas as pd
from reverse_geocoder import ReverseGeocoder

class GeocodeDataFrame:
    def __init__(self, df):
        self.df = df

    def geocode(self):
        addresses = []

        for index, row in self.df.iterrows():
            # get the latitude and longitude values from the DataFrame
            lat = row['latitude']
            lon = row['longitude']

            # create a ReverseGeocoder instance
            geocoder = ReverseGeocoder(lat, lon)

            # get the address components
            address_components = geocoder.get_address()
            print(address_components)
            address = address_components['address']

            # append the address components to the lists
            addresses.append(address)

        # add the new columns to the DataFrame
        self.df['address'] = addresses
        
        return self.df
