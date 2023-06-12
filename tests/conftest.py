import pytest
import requests
from configuration import GEODATA_URL


def _create_url_part(request_type, street, city, format_url):

    return request_type + street.replace(' ', '%20')+'%20' + city + format_url


def _request_address(url_part):
    response = requests.get(GEODATA_URL+url_part)

    return response


@pytest.fixture()
def create_url_part():
    return _create_url_part


@pytest.fixture()
def request_address():
    return _request_address
