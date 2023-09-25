from argparser import ArgParser
from daos import CountryPsycopg2DAO, CountrySQLAlchemyDAO


class CountryModel():
    def __init__(self):
        self.__country_id = None
        self.__country = None
        self.__last_update = None

        self.__available_DAOs = {
            "orm": CountrySQLAlchemyDAO,
            "driver": CountryPsycopg2DAO
        }

        self.__DAO = self.__available_DAOs[ArgParser().get_args().dam]()

    def __str__(self):
        return f"country_id: {self.__country_id}\n" \
            f"country: {self.__country}\n" \
            f"last_update: {self.__last_update}\n"

    def create(self, country_id, country, last_update):
        pass

    def read_by_id(self, country_id):
        pass

    def read_by_name(self, country):
        data = self.__DAO.read_by_name(country)

        if data is None:
            return None

        self.__country_id = data['country_id']
        self.__country = data['country']
        self.__last_update = data['last_update']

        return self

    def update(self, data):
        pass

    def delete(self):
        pass

    def get_country_id(self):
        return self.__country_id

    def get_country(self):
        return self.__country

    def get_last_update(self):
        return self.__last_update
