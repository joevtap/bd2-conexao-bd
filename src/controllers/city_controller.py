from datetime import datetime
from typing import Dict
from models.city_model import CityModel


class CityController():
    def __init__(self):
        pass

    # TODO: Type datetime.datetime is suitable for this?
    def create(self, city_id: int, city: str, country_id: int, last_update: datetime) -> bool:
        return CityModel().create(city_id, city, country_id, last_update)

    def read_by_id(self, city_id: int) -> CityModel:
        return CityModel().read_by_id(city_id)

    def read_by_name(self, city: str) -> CityModel:
        return CityModel().read_by_name(city)

    def list_by_country_name(self, country_name: str) -> Dict[str or int or datetime]:
        # country = CountryModel().read_by_name(country_name)
        # return self.__DAO.list_by_country_id(country.get_country_id())
        pass

    def update(self, city: str, data: Dict[str, datetime or str or int]) -> CityModel:
        curr_city = CityModel().read_by_name(city)
        return curr_city.update(data)

    def delete(self, city: str) -> bool:
        city = CityModel().read_by_name(city)
        return city.delete()
