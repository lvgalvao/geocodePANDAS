import pytest
from geocodepandas.reverse_geocoder import ReverseGeocoder

def test_reverse_geocoder():
    # create a ReverseGeocoder instance
    geocoder = ReverseGeocoder(37.7749, -122.4194)

    # get the address components
    address_components = geocoder.get_address()

    # check that the address components are correct
    assert address_components['address'] == '944 Market Street, Westfield San Francisco Centre, San Francisco, California, 94102, USA'
    assert address_components['city'] == 'San Francisco'
    assert address_components['state'] == 'California'

def test_reverse_geocoder_error():
    # create a ReverseGeocoder instance with invalid latitude and longitude values
    geocoder = ReverseGeocoder(9999, -9999)

    # get the address components
    address_components = geocoder.get_address()

    # check that the address components are empty
    assert address_components['address'] == ''
    assert address_components['city'] == ''
    assert address_components['state'] == ''