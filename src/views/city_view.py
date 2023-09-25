from argparser import ArgParser
from datetime import datetime
from utils import console_clear, get_numeric_input


class CityView():
    def __init__(self, main_controller, controller):
        self.__main_controller = main_controller
        self.__controller = controller()

    def run(self):
        console_clear()
        print("CRUD for table City", end="\n")
        print(
            f"Current Database Access Method and DAO: {ArgParser().get_args().dam}", end="\n\n")
        print(40 * "=", end="\n\n")
        print("Choose an option:", end="\n\n")
        print("1. Insert a new city")
        print("2. Update a city")
        print("3. Delete a city")
        print("4. Show city data")
        print("5. List cities in country")
        print("6. Back", end="\n\n")

        option = get_numeric_input(">>> ", 0)

        if option == 1:
            console_clear()
            print("Insert a new city")

            city_id = get_numeric_input("City ID: ")
            city = input("City: ")
            country_id = get_numeric_input("Country ID: ")
            last_update = datetime.now()

            if (city_id is None or not int) or (city is None or not str) or (country_id is None or not int):
                self.run()

            try:
                print(self.__controller.create(
                    city_id, city, country_id, last_update))
            except Exception as e:
                print(e)
            finally:
                input("Press enter to continue...")
                self.run()

        elif option == 2:
            console_clear()
            print("Update a city")

            city_id = get_numeric_input("City ID: ")
            print(f"Trying to update city with ID: {city_id}")
            city = input("City: ")
            country_id = get_numeric_input("Country ID: ")
            last_update = datetime.now()

            if (city_id is None or not int) or (city is None or not str) or (country_id is None or not int):
                self.run()

            try:
                found = self.__controller.update(
                    city_id, city, country_id, last_update)
                if found is None:
                    print(f"City \"{city}\" does not exist!")
                else:
                    print(found)
            except Exception as e:
                print(e)
            finally:
                input("Press enter to continue...")
                self.run()

        elif option == 3:
            console_clear()
            print("Delete a city")

            city = input("City: ")

            if city is None or not int:
                self.run()

            try:
                found = self.__controller.delete(city)
                if found is None:
                    print(f"City \"{city}\" does not exist!")
                else:
                    print(found)
            except Exception as e:
                print(e)
            finally:
                input("Press enter to continue...")
                self.run()

        elif option == 4:
            console_clear()
            print("Show city data")
            city = input("City: ")

            if city is None or not str:
                self.run()

            try:
                found = self.__controller.read_by_name(city)
                if found is None:
                    print(f"City \"{city}\" not found!")
                else:
                    print(found)
            except Exception as e:
                print(e)
            finally:
                input("Press enter to continue...")
                self.run()

        elif option == 5:
            console_clear()
            print("List cities in country")

            country = input("Country: ")

            if country is None or not str:
                self.run()

            list = self.__controller.list_by_country_name(country)

            if list is None:
                print(f"Country {country} not found!")
            else:
                for city in list:
                    print(city)

            input("Press enter to continue...")

            self.run()

        elif option == 6:
            self.__main_controller.change_view("main")

        else:
            self.run()
