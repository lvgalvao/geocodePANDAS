import pandas as pd
import numpy as np

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        # read the CSV file into a pandas DataFrame
        df = pd.read_csv(self.file_path, usecols=['id_store', 'latitude', 'longitude', 'country'])
                                                  
        colunas = ['display_name', 'road', 'house_number', 'city', 'state', 'suburb', 'postcode', 'category', 'type', 'osm_type', 'osm_id']

        # to check if a CSV file has specific columns and create them with null values if they don't exis
        for col in colunas:
            if col not in df.columns:
                df[col] = np.nan

        return df
    

    
    def save_csv(self, df, output_file_path):
        # save the DataFrame to a CSV file
        df.to_csv(output_file_path, index=False)
        


