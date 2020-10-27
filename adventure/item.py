from enum import Enum, auto


class Capable(Enum):
    READ = auto()
    FIGHT = auto()
    FOOD = auto()


class Item:
    def __init__(self, name, description="", capable=None):
        self.__name = name
        self.__description = description
        self.capable = capable
        self.usage: str = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, item_name):
        self.__name = item_name.title()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, info):
        self.__description = info

    def describe(self):
        print("* "+self.__name+": "+self.__description)

    def use(self, action=None):
        if self.capable == Capable.READ:
            self.read()
        else:
            print(f"< {self.name} cannot be used")

    def read(self):
        print(self.usage)