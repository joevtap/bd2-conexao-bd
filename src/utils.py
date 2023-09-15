import os


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_numeric_input(message, default_value=None):
    try:
        return int(input(message) or default_value)
    except ValueError:
        return default_value
