import pytest
import requests
from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path
from configuration import GEODATA_URL
from utils.util import get_data



featureFile = 'getAddress.feature'
featureDirectory = 'getDataFeature'

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.joinpath(featureDirectory).joinpath(featureFile)
format_url = '?format=jsonv2&'
target_lat,target_lon = '52.51720765', '13.397834399325466'
target_street, target_house_number = 'Unter den Linden', '1'


@scenario(DATA_FILE, 'Determine the address by reverse geocoding')
def test_getting_address():
    print('End of the getting address')
    pass
@given('I send coordinates')
def send_place():
    pytest.place_to_parse = requests.get(GEODATA_URL + 'reverse/'+format_url +
                                         f'lat={target_lat}&'+f'lon={target_lon}')
@when('I am try to get address')
def get_address():
    pytest.street = pytest.place_to_parse.json()['address']['road']
    pytest.house_number = pytest.place_to_parse.json()['address']['house_number']

@then('I should see correct coordinates address')
def check_address():
    assert pytest.street == target_street and pytest.house_number == target_house_number
