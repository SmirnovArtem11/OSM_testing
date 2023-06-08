from src.schemas.place import Place

place1 = 'search/Unter%20den%20Linden%201%20Berlin?format=json&addressdetails=1&limit=1&polygon_svg=1'


def test_getting_place(request_address):

    assert request_address(place1).status_code == 200, 'address not valid'
    print(request_address)


def test_validate_place(request_address):
    print(request_address(place1).json()[0])
    assert Place.parse_obj(request_address(place1).json()[0]), 'address not valid'
    print(Place.parse_obj(request_address(place1).json()[0]))

