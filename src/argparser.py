import argparse


class ArgParserMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                ArgParserMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ArgParser(metaclass=ArgParserMeta):
    def __init__(self):
        self.__parser = argparse.ArgumentParser(description='CRUD APP')
        self.__parser.add_argument('--dam', type=str, default='orm',
                                   help='Database Access Method to use (orm or driver)')
        self.__args = self.__parser.parse_args()
        self.__validate_args()

    def get_args(self):
        return self.__args

    def __validate_args(self):
        if self.__args.dam not in ['orm', 'driver']:
            raise ValueError('dam must be `orm` or `driver`')
