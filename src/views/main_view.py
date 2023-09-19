from controllers.city_controller import CityController
from utils import console_clear, get_numeric_input


class MainView():
    def __init__(self, main_controller, _):
        self.__controller = main_controller

    def run(self):
        console_clear()
        print("Choose an option:", end="\n\n")
        print("1. CRUD for City")
        print("2. Exit", end="\n\n")

        option = get_numeric_input(">>> ", 0)

        if option == 1:
            self.__controller.change_view("city", CityController)
        elif option == 2:
            self.__controller.exit()
        else:
            self.run()
