from typing import Dict, Callable
from adventure.character import BattleOutcome, Friend


class Command:
    def __init__(self, scene):
        self._scene = scene
        self.commands: Dict[str, str] = {}
        self._commands: Dict[str, Dict[str, str]] = {}
        self._exec: Dict[str, Callable] = {}
        self.register()

    def register(self):
        """
        command dict: "key to recognise": "command name"
        """
        directions = {
            "east": "east",
            "e": "east",
            "west": "west",
            "w": "west",
            "north": "north",
            "n": "north",
            "south": "south",
            "s": "south",
        }
        self._commands["directions"] = directions
        self._exec["directions"] = self.move

        talks = {"talk": "talk", "t": "talk"}
        self._commands["talk"] = talks
        self._exec["talk"] = self.talk

        fights = {"fight": "fight", "f": "fight"}
        self._commands["fight"] = fights
        self._exec["fight"] = self.fight

        looks = {"look": "look", "l": "look"}
        self._commands["look"] = looks
        self._exec["look"] = self.look

        helps = {"help": "help", "h": "help"}
        self._commands["help"] = helps
        self._exec["help"] = self.help

        items = {"item": "item", "i": "item"}
        self._commands["item"] = items
        self._exec["item"] = self.backpacking

        probes = {"probe": "probe", "p": "probe"}
        self._commands["probe"] = probes
        self._exec["probe"] = self.probe

        grabs = {"grab": "grab", "g": "grab"}
        self._commands["grab"] = grabs
        self._exec["grab"] = self.grab

        uses = {"use": "use", "u": "use"}
        self._commands["use"] = uses
        self._exec["use"] = self.use

        for command_group in self._commands:
            self.commands.update(self._commands[command_group])

    def exec(self, action):
        for command_group in self._commands:
            if action in set(self._commands[command_group]):
                self._exec[command_group](action)

    def use(self, action=None):
        items = self._scene.backpack
        if len(items) == 0:
            print("< No item to use")
        elif len(items) >= 1:
            item = self.choose_obj(items)

            if item is None:
                return
            else:
                item.use(action)

    def probe(self, action=None):
        furnitures = self._scene.room.furnitures
        if len(furnitures) == 0:
            print("< No furniture to probe")
        elif len(furnitures) >= 1:
            furniture = self.choose_obj(furnitures)

            if furniture is None:
                return
            else:
                item = furniture.probe()
                if item:
                    self._scene.room.items.append(item)

    def grab(self, action=None):
        items = self._scene.room.items
        if len(items) == 0:
            print("< No item to grab")
        elif len(items) >= 1:
            item = self.choose_obj(items)

            if item is None:
                return
            else:
                self._scene.backpack.append(item)
                self._scene.room.items.remove(item)
                print(f"< grab {item.name}")

    def backpacking(self, action=None):
        if self._scene.backpack:
            items = [item.name.title() for item in self._scene.backpack]
            print("$ In backpack:", ", ".join(items))
        else:
            print("$ Backpack is empty")

    def help(self, action=None):
        print(self._scene.help)

    def look(self, action=None):
        self._scene.room.info()

    def move(self, direction=None):
        if self._scene.room is None:
            print("< You need a room to start moving.")
            return
        if direction in self._commands["directions"]:
            real_direction = self._commands["directions"][direction]
            if real_direction in self._scene.room.linked_rooms:
                self._scene.room = self._scene.room.linked_rooms[real_direction]
                self._scene.room.info()
            else:
                print("You can't go that way")

    def choose_obj(self, obj)->int:
        if len(obj) == 1:
            return obj[0]
        for n, character in enumerate(obj):
            if len(obj) > 1:
                print(f"[{n}]: {character.name}")
        try:
            n_character = int(input(f">> Which option: "))
        except ValueError:
            print("< Unknown choice")
        else:
            if 0 <= n_character < len(obj):
                return obj[n_character]
            else:
                print("< Unknown choice")

    def talk(self, action=None):
        characters = self._scene.room.characters
        if len(characters) == 0:
            print("< No one can hear you")
        elif len(characters) >= 1:
            talker = self.choose_obj(characters)

            if talker is None:
                return
            elif isinstance(talker, Friend):
                gift = talker.talk()
                if gift:
                    self._scene.backpack.append(gift)
            else:
                talker.talk()

    def fight(self, action: None):
        characters = self._scene.room.characters
        if len(characters) == 0:
            print("< No one can fight with you")
        elif len(characters) >= 1:
            fighter = self.choose_obj(characters)
            if fighter is None:
                return
            else:
                result = fighter.fight()

            if result == BattleOutcome.WIN:
                self._scene.room.characters.remove(fighter)
                self._scene.score += 1
            elif result == BattleOutcome.LOSS:
                self._scene.health -= 1
