import time
from utils import console_clear, get_chosen_dam
from views.city_view import CityView
from views.main_view import MainView
from controllers.main_controller import MainController


def main():
    console_clear()
    print(
        f"Using \"{get_chosen_dam()}\" Database Access Method and DAO", end="\n\n")

    time.sleep(1)

    views = {
        "main": MainView,
        "city": CityView
    }

    MainController(views)


if __name__ == '__main__':
    main()
