import pytest
import requests
from configuration import GEODATA_URL


def _request_address(url_part):
    response = requests.get(GEODATA_URL+url_part)

    return response
@pytest.fixture()
def request_address():
    return _request_address
