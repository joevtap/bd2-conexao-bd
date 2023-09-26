import sqlalchemy
import os
from sqlalchemy.ext.automap import automap_base


class CitySQLAlchemyDAO():
    def __init__(self):
        url = sqlalchemy.URL.create(
            'postgresql+psycopg2',
            username=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('APP_DB')
        )

        self.__engine = sqlalchemy.create_engine(url, echo=False)

        self.__base = automap_base()
        self.__base.prepare(self.__engine, schema='public', reflect=True)

        self.__city = self.__base.classes.city

        Session = sqlalchemy.orm.sessionmaker(bind=self.__engine)
        self.__session = Session()

    def create(self, city_id, city, country_id, last_update):
        try:
            data = self.__city(
                city_id=city_id,
                city=city,
                country_id=country_id,
                last_update=last_update
            )

            self.__session.add(data)
            self.__session.commit()

        except Exception as e:
            raise e

        if data is None:
            return None
        else:
            return self.__parse_data(data)

    def read_by_id(self, city_id):
        try:
            data = self.__session.query(self.__city).filter(
                self.__city.city_id == city_id).first()

        except Exception as e:
            raise e

        if data is None:
            return None
        else:
            self.__session.commit()
            return self.__parse_data(data)

    def read_by_name(self, city):
        try:
            data = self.__session.query(self.__city).filter(
                self.__city.city == city).first()
        except Exception as e:
            raise e

        if data is None:
            return None
        else:
            self.__session.commit()
            return self.__parse_data(data)

    def list_by_country_id(self, country_id):
        try:
            data = self.__session.query(self.__city).filter(
                self.__city.country_id == country_id).all()
        except Exception as e:
            raise e

        if data is None:
            return None
        else:
            self.__session.commit()
            return [self.__parse_data(city) for city in data]

    def update(self, city_id, city, country_id, last_update):
        try:
            data = self.__session.query(self.__city).filter(
                self.__city.city_id == city_id).first()
        except Exception as e:
            raise e

        if data is None:
            return None
        else:

            data.city = city
            data.country_id = country_id
            data.last_update = last_update

            self.__session.commit()
            return self.__parse_data(data)

    def delete(self, city_id):
        try:
            data = self.__session.query(self.__city).filter(
                self.__city.city_id == city_id).first()
        except Exception as e:
            raise e

        if data is None:
            return None
        else:
            self.__session.delete(data)
            self.__session.commit()
            return self.__parse_data(data)

    def __parse_data(self, data):
        return {
            'city_id': data.city_id,
            'city': data.city,
            'country_id': data.country_id,
            'last_update': data.last_update
        }
