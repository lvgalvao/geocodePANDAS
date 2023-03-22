# Geocode Stores

Geocode Stores is a Python script that reads a CSV file containing store information, including latitude and longitude coordinates, and retrieves additional address information using the Nominatim OpenStreetMap API. The enriched store data is then saved to an output CSV file.

## Requirements and Installation
- Python 3.6 or later
- Poetry library
- Pandas library
- Requests library

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install the project, first install Poetry:

```bash
pip install poetry
````

Next, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your_username/geocodepandas.git
cd geocodepandas
```

Install the project and its dependencies using Poetry:

```bash
poetry install
```

## Usage

First, make sure your input CSV file contains at least the following columns:

- id_store
- latitude
- longitude
- country
  
Then, call the process_stores function in your script with the input and output file paths, and an optional country filter:

```python
from geocode_stores import process_stores

input_file = 'input/stores.csv'
output_file = 'output/update_stores_br.csv'
country_filter = 'BR'

process_stores(input_file, output_file, country_filter)

```

The script will process the input file, filtering by the specified country if provided, and retrieve address information using the Nominatim API for stores with missing display_name values. The resulting data will be saved to the specified output file.


## Modules

The project consists of the following modules:

- `reverse_geocoder.py`: Contains the `ReverseGeocoder` class, which is responsible for sending requests to the Nominatim API and parsing the response.
- `read_csv.py`: Contains the `CSVReader` class, which is responsible for reading the input CSV file, adding missing address columns, and saving the processed data to an output file.
- `geocode_stores.py`: Contains the main functionality of the script, using the `ReverseGeocoder` and `CSVReader` classes to retrieve address information and process the store data.