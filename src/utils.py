import os
import argparse


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_numeric_input(message, default_value=None):
    try:
        return int(input(message) or default_value)
    except ValueError:
        return default_value


def get_choosen_dam():
    parser = argparse.ArgumentParser(description='CRUD APP')
    parser.add_argument('--dam', type=str, default='orm',
                        help='Database Access Method to use (orm or driver)')
    args = parser.parse_args()

    if args.dam not in ['orm', 'driver']:
        raise ValueError("Invalid Database Access Method")

    return args.dam
