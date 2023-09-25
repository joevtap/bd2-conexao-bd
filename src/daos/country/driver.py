import psycopg2
import os


class CountryPsycopg2DAO():
    def __init__(self):
        self.__connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database='pagila',
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD')
        )

    def create(self, country_id, country, last_update):
        pass

    def read_by_id(self, country_id):
        pass

    def read_by_name(self, country):
        cursor = self.__connection.cursor()

        try:
            cursor.execute(
                'SELECT * FROM country WHERE country = %s', (country,)
            )

            data = cursor.fetchone()

            cursor.close()

        except Exception as e:
            raise e

        if data is None:
            return None
        else:
            return self.__parse_data(data)

    def update(self,  country_id, country, last_update):
        pass

    def delete(self, country_id):
        pass

    def __parse_data(self, data):
        return {
            'country_id': data[0],
            'country': data[1],
            'last_update': data[2]
        }
