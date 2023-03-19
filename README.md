# GeocodePandas

GeocodePandas is a Python library that allows you to easily geocode and reverse geocode addresses using latitude and longitude coordinates in pandas DataFrames. It simplifies the process of adding address information to your data by providing simple-to-use classes.

## Features

- Read CSV files containing latitude and longitude coordinates
- Geocode and reverse geocode addresses using a custom `ReverseGeocoder` class
- Add address information to pandas DataFrames
- Save updated DataFrames to new CSV files
- Easily testable with pytest

## Installation

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
To use GeocodePandas, first import the necessary classes:

```python
from geocodepandas import GeocodeDataFrame
from geocodepandas import CSVReader
```

Read a CSV file with latitude and longitude coordinates using the CSVReader class:

```python
reader = CSVReader('assets/stores.csv')
df = reader.read_csv()
```

Create a GeocodeDataFrame instance and geocode the DataFrame:

```python
geocode_df = GeocodeDataFrame(df)
result_df = geocode_df.geocode()
```

Save the updated DataFrame to a new CSV file:

```python
reader.save_csv(result_df, 'updated_stores.csv')
```
