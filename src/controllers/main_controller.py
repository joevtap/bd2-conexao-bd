import os


class MainController():
    def __init__(self, views):
        self.__views = views
        self.change_view("main")

    def change_view(self, view_name, controller=None):
        if view_name in self.__views:
            self.__view = self.__views[view_name]
        else:
            raise ValueError("View not found")

        self.__view(self, controller).run()

    def exit(self):
        os._exit(0)
