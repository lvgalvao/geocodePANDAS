from geocode_stores import process_stores

input_file = 'input/stores.csv'
output_file = 'output/update_stores_br.csv'
country_filter = 'BR'

process_stores(input_file, output_file, country_filter)