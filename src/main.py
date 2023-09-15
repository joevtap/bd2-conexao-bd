from views.city_view import CityView
from views.main_view import MainView
from controllers.main_controller import MainController


def main():
    views = {
        "main": MainView,
        "city": CityView
    }

    MainController(views)


if __name__ == '__main__':
    main()
