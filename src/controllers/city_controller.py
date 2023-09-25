from models.city_model import CityModel


class CityController():
    def __init__(self):
        pass

    def create(self, city_id, city, country_id, last_update) -> bool:
        return CityModel().create(city_id, city, country_id, last_update)

    def read_by_id(self, city_id) -> CityModel:
        return CityModel().read_by_id(city_id)

    def read_by_name(self, city) -> CityModel:
        return CityModel().read_by_name(city)

    def list_by_country_name(self, country_name):
        # country = CountryModel().read_by_name(country_name)
        # return self.__DAO.list_by_country_id(country.get_country_id())
        pass

    def update(self, city_id, city, country_id, last_update) -> CityModel:
        curr_city = CityModel().read_by_id(city_id)
        return curr_city.update(city, country_id, last_update)

    def delete(self, city: str) -> bool:
        city = CityModel().read_by_name(city)

        if city is None:
            return None

        return city.delete()
