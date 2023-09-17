import datetime
from typing import List, Dict
from utils import get_chosen_dam


class CityModel():
    def __init__(self):
        self.__city_id = None
        self.__city = None
        self.__country_id = None
        self.__last_update = None

        self.__available_DAOs = {
            # "orm": CitySQLAlchemyDAO,
            # "driver": CityPsycopg2DAO
        }

        self.__DAO = self.__available_DAOs[get_chosen_dam()]()

    def __str__(self):
        return f"city_id: {self.__city_id}\n" \
            f"city: {self.__city}\n" \
            f"country_id: {self.__country_id}\n" \
            f"last_update: {self.__last_update}\n"

    def create(self, city_id, city, country_id, last_update):
        self.__city_id = city_id
        self.__city = city
        self.__country_id = country_id
        self.__last_update = last_update

        return self.__DAO.create(self.__city_id, self.__city,
                                 self.__country_id, self.__last_update)

    def read_by_id(self, city_id):
        data = self.__DAO.read_by_id(city_id)

        self.__city_id = data['city_id']
        self.__city = data['city']
        self.__country_id = data['country_id']
        self.__last_update = data['last_update']

        return self

    def read_by_name(self, city):
        data = self.__DAO.read_by_name(city)

        self.__city_id = data['city_id']
        self.__city = data['city']
        self.__country_id = data['country_id']
        self.__last_update = data['last_update']

        return self

    def list_by_country_id(self, country_id) -> List[Dict[str or int or datetime]]:
        data = self.__DAO.list_by_country_id(country_id)

        return data

    def update(self, data):
        data = self.__DAO.update(self.__city_id, data)

        self.__city_id = data['city_id']
        self.__city = data['city']
        self.__country_id = data['country_id']
        self.__last_update = data['last_update']

        return self

    def delete(self):
        return self.__DAO.delete(self.__city_id)

    def get_city_id(self):
        return self.__city_id

    def get_city(self):
        return self.__city

    def get_country_id(self):
        return self.__country_id

    def get_last_update(self):
        return self.__last_update
