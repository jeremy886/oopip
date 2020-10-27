from typing import List
from random import shuffle

from adventure.item import Item


class Room:
    __opposite = {
        "east": "west",
        "west": "east",
        "north": "south",
        "south": "north",
    }

    def __init__(self, name: str, description=""):
        self.name: str = name.title()
        self.description: str = description
        self.linked_rooms: Room = {}
        self.characters = []
        self.furnitures = []
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, room_name):
        self.__name = room_name.title()

    # @property
    # def description(self):
    #     return self.__description
    #
    # @description.setter
    # def description(self, info):
    #     self.__description = info

    def describe(self):
        print(self.__name + ": " + self.description)

    def info(self):
        print(self.__name)
        print("-" * 40)
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"+ The {room.name.title()} is {direction}")
        for character in self.characters:
            character.describe()
        for furniture in self.furnitures:
            furniture.describe()
        for item in self.items:
            item.describe()

    def link_room(self, room, direction, two_way=True):
        self.linked_rooms[direction] = room

        if two_way:
            room.link_room(self, self.__opposite[direction], False)


class Furniture:
    def __init__(self, name, description, items=None):
        self.name:str = name
        self.description:str = description
        self.items: List[Item] = items or []

    def describe(self):
        print(f"* {self.name}: {self.description}")

    def probe(self):
        if self.items:
            shuffle(self.items)
            item_revealed = self.items.pop()
            print(f'< {self.name} was probed and "{item_revealed.name}" was found')
            return item_revealed
        else:
            print(f"< {self.name} was probed and nothing found")
