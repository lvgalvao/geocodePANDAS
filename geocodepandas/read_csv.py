import pandas as pd
import numpy as np

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def _read_csv(self):
        # Read the CSV file into a pandas DataFrame
        try:
            df = pd.read_csv(self.file_path, usecols=['storeid', 'lat', 'lon', 'country','display_name', 'road', 'house_number', 'city', 'state', 'suburb', 'postcode', 'category', 'type', 'osm_type', 'osm_id'])
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return None
        return df

    @staticmethod
    def _add_missing_columns(df, columns):
        # Check if a CSV file has specific columns and create them with null values if they don't exist
        for col in columns:
            if col not in df.columns:
                df[col] = np.nan
        return df

    def process_csv(self):
        df = self._read_csv()
        if df is not None:
            columns = ['display_name', 'road', 'house_number', 'city', 'state', 'suburb', 'postcode', 'category', 'type', 'osm_type', 'osm_id']
            df = self._add_missing_columns(df, columns)
        return df

    def save_csv(self, df, output_file_path):
        """
        Save the DataFrame to a CSV file
        """
        if df is not None:
            # Save the DataFrame to a CSV file
            df.to_csv(output_file_path, index=False)
        else:
            print("No DataFrame to save")