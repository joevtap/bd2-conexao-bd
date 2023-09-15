from utils import console_clear, get_numeric_input


class CityView():
    def __init__(self, main_controller, controller):
        self.__main_controller = main_controller
        self.__controller = controller

    def run(self):
        console_clear()
        print("CRUD for table City", end="\n\n")
        print(20 * "=", end="\n\n")
        print("Choose an option:", end="\n\n")
        print("1. Insert a new city")
        print("2. Update a city")
        print("3. Delete a city")
        print("4. Show city data")
        print("5. List cities in country")
        print("6. Back", end="\n\n")

        option = get_numeric_input(">>> ", 0)

        if option == 1:
            print("CRUD")
            self.run()

        elif option == 2:
            print("CRUD")
            self.run()

        elif option == 3:
            print("CRUD")
            self.run()

        elif option == 4:
            print("CRUD")
            self.run()

        elif option == 5:
            print("CRUD")
            self.run()

        elif option == 6:
            self.__main_controller.change_view("main")

        else:
            self.run()
