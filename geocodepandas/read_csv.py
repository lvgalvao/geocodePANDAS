import pandas as pd

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        # read the CSV file into a pandas DataFrame
        df = pd.read_csv(self.file_path, usecols=['id_store', 'latitude', 'longitude', 'country'])
        return df
    
    def save_csv(self, df, output_file_path):
        # save the DataFrame to a CSV file
        df.to_csv(output_file_path, index=False)
        


