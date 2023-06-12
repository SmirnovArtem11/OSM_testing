import pytest

from src.schemas.place import Place
from utils.util import get_data, create_data

format_url = '?format=json&addressdetails=1&limit=1&polygon_svg=1'
data_with_coordinates = []
def add_suplist(list):
    data_with_coordinates.append(list)


@pytest.mark.parametrize('id, street, city, lat, lon', get_data())
class TestGettingDataByAddress:

    '''Проверяем ответ для каждого адреса'''
    def test_getting_place(self, id, street, city, lat, lon,request_address, create_url_part):
        place_to_parse = create_url_part('search/', street, city, format_url)
        assert request_address(place_to_parse).status_code == 200, 'address not valid'

    '''Проверяем содержимое джсона, если есть ответ'''
    def test_validate_place(self, id, street, city, lat, lon, request_address, create_url_part):
        place_to_parse = create_url_part('search/', street, city, format_url)
        if request_address(place_to_parse).status_code != 200:
            pytest.skip('No data to validate')

        lon = request_address(place_to_parse).json()[0]['lon']
        lat = request_address(place_to_parse).json()[0]['lat']
        add_suplist((id, street, city, lat, lon))

        assert Place.parse_obj(request_address(place_to_parse).json()[0]), 'address not valid'


def test_new_data():
    assert data_with_coordinates != [], 'lat and lon not added'
    create_data(data_with_coordinates)
    create_data(data_with_coordinates)
    '''Записываем координаты для адресов'''

