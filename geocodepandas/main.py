import pandas as pd
from data_transformations import extract_city, extract_state

# Load the CSV file
input_file = 'files/setNewAddress_Discovery_Latam.csv'
df = pd.read_csv(input_file)

# Perform city extraction
df = extract_city(df)

# Perform state extraction
df = extract_state(df)

# Save the results to a new CSV file
output_file = 'files/setNewAddress_Discovery_Latam_full.csv'
df.to_csv(output_file, index=False)

print("Data processing completed. Results saved to", output_file)