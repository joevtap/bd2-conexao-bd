import sqlalchemy
import os
from sqlalchemy.ext.automap import automap_base


class CountrySQLAlchemyDAO():
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

        self.__country = self.__base.classes.country

        Session = sqlalchemy.orm.sessionmaker(bind=self.__engine)
        self.__session = Session()

    def create(self, country_id, country, last_update):
        pass

    def read_by_id(self, country_id):
        pass

    def read_by_name(self, country):
        try:
            data = self.__session.query(self.__country).filter(
                self.__country.country == country).first()
        except Exception as e:
            raise e

        if data is None:
            return None
        else:
            self.__session.commit()
            return self.__parse_data(data)

    def update(self, country_id, country,  last_update):
        pass

    def delete(self, country_id):
        pass

    def __parse_data(self, data):
        return {
            'country_id': data.country_id,
            'country': data.country,
            'last_update': data.last_update
        }
