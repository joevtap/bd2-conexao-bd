import time
from argparser import ArgParser
from utils import console_clear
from views.city_view import CityView
from views.main_view import MainView
from controllers.main_controller import MainController
from dotenv import load_dotenv


def main():
    load_dotenv()
    argparser = ArgParser()

    console_clear()
    print(
        f"Using \"{argparser.get_args().dam}\" Database Access Method and DAO", end="\n\n")

    time.sleep(1)

    MainController(views={
        'main': MainView,
        'city': CityView
    })


if __name__ == '__main__':
    main()
