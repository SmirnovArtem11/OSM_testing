from pydantic import BaseModel


# Create class to address elements without 'ISO3166-2-lvl4'
class Address(BaseModel):
    house_number: str
    road: str
    neighbourhood: str
    suburb: str
    borough: str
    city: str
    postcode: str
    country: str
    country_code: str


# Create class to check GET options
class Place(BaseModel):
    place_id: int
    lat: str
    lon: str
    display_name: str
    type: str

    address: Address
