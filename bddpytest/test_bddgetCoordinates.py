import pytest
import requests
from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path
from configuration import GEODATA_URL
from utils.util import get_data



featureFile = 'getCoordinates.feature'
featureDirectory = 'getDataFeature'

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.joinpath(featureDirectory).joinpath(featureFile)
format_url = '?format=json&addressdetails=1&limit=1&polygon_svg=1'
target_lat,target_lon = '52.51720765', '13.397834399325466'


@scenario(DATA_FILE, 'Determine coordinates by search queries')
def test_getting_coordinates():
    print('End of the getting coordinates')
    pass
@given('I send the address')
def send_place():
    pytest.place_to_parse = requests.get(GEODATA_URL + 'search/'+'Unter%20den%20Linden%201%20Berlin'+format_url)
@when('I am try to get coordinates')
def get_coordinates():
    pytest.lon = pytest.place_to_parse.json()[0]['lon']
    pytest.lat = pytest.place_to_parse.json()[0]['lat']

@then('I should see the correct coordinates')
def check_coordinates():
    assert pytest.lat == target_lat and pytest.lon == target_lon



