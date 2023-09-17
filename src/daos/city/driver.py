import psycopg2
import os


class CityPsycopg2DAO():
    def __init__(self):
        self.__connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database='pagila',
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD')
        )

    def create(self, city_id, city, country_id, last_update):
        cursor = self.__connection.cursor()

        try:
            cursor.execute(
                'INSERT INTO city (city_id, city, country_id, last_update) VALUES (%s, %s, %s, %s) RETURNING *', (city_id,
                                                                                                                  city, country_id, last_update)
            )

            data = cursor.fetchone()

            self.__connection.commit()

            cursor.close()

        except psycopg2.errors.UniqueViolation:
            cursor.close()
            return None

        except psycopg2.errors.ForeignKeyViolation:
            cursor.close()
            return None

        except:
            cursor.close()
            return None

        if data is None:
            return None
        else:
            return self.__parse_data(data)

    def read_by_id(self, city_id):
        cursor = self.__connection.cursor()

        try:
            cursor.execute(
                'SELECT * FROM city WHERE city_id = %s', (city_id,)
            )

            data = cursor.fetchone()

            cursor.close()

        except:
            cursor.close()
            return None

        if data is None:
            return None
        else:
            return self.__parse_data(data)

    def read_by_name(self, city):
        cursor = self.__connection.cursor()

        try:
            cursor.execute(
                'SELECT * FROM city WHERE city = %s', (city,)
            )

            data = cursor.fetchone()

            cursor.close()

        except:
            cursor.close()
            return None

        if data is None:
            return None
        else:
            return self.__parse_data(data)

    def list_by_country_id(self, country_id):
        cursor = self.__connection.cursor()

        try:
            cursor.execute(
                'SELECT * FROM city WHERE country_id = %s', (country_id,)
            )

            data = cursor.fetchall()

            cursor.close()

        except:
            cursor.close()
            return None

        if data is None:
            return None
        else:
            return [self.__parse_data(city) for city in data]

    def update(self, city_id, city, country_id, last_update):
        cursor = self.__connection.cursor()

        try:
            cursor.execute(
                'UPDATE city SET city = %s, country_id = %s, last_update = %s WHERE city_id = %s RETURNING *', (
                    city, country_id, last_update, city_id)
            )

            data = cursor.fetchone()

            self.__connection.commit()

            cursor.close()

        except psycopg2.errors.UniqueViolation:
            cursor.close()
            return None

        except psycopg2.errors.ForeignKeyViolation:
            cursor.close()
            return None

        except:
            cursor.close()
            return None

        if data is None:
            return None
        else:
            return self.__parse_data(data)

    def delete(self, city_id):
        cursor = self.__connection.cursor()

        try:
            cursor.execute(
                'DELETE FROM city WHERE city_id = %s RETURNING *', (city_id,)
            )

            data = cursor.fetchone()

            self.__connection.commit()

            cursor.close()

        except:
            cursor.close()
            return None

        if data is None:
            return None
        else:
            return self.__parse_data(data)

    def __parse_data(self, data):
        return {
            'city_id': data[0],
            'city': data[1],
            'country_id': data[2],
            'last_update': data[3]
        }
