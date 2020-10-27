from typing import List
from enum import Enum, auto
from adventure.challenge import Challenge
from adventure.item import Item


class BattleOutcome(Enum):
    WIN = auto()
    LOSS = auto()
    DRAW = auto()


class Character:
    def __init__(
        self,
        name,
        description="a character",
        conversation=None,
    ):
        """
        weakness is a dict of quiz {"question": "answer"}
        """
        self.name = name
        self.description = description
        self.conversation = conversation

    def describe(self):
        print(f"@ {self.name} is here!")
        print(f"  {self.description}")

    def talk(self):
        if self.conversation:
            for n, line in enumerate(self.conversation.splitlines()):
                if n == 0:
                    print(f"[{self.name} says] {line}")
                else:
                    print(f"{' '*(len(self.name)+8)}{line}")
        else:
            print(f"{self.name} doesn't want to talk to you")

    def fight(self):
        print(f"{self.name} doesn't want to fight with you")
        return 0


class Enemy(Character):
    def __init__(
        self,
        name: str,
        description: str = "a smelly zombie ",
        conversation: str = "",
        challenge=Challenge(),
    ):
        super().__init__(name, description, conversation)
        self.challenge = challenge

    def describe(self):
        print(f"@ {self.name} is here!")
        print(f"  {self.description}")

    def fight(self):
        print(f"[{self.name} attacks] ", self.challenge.quiz)
        response = input("response>> ")
        if response in self.challenge.ans:
            print(f"You fend {self.name} off successfully")
            return BattleOutcome.WIN
        else:
            print(f"{self.name} crushes you, punny adventurer")
            return BattleOutcome.LOSS


class Friend(Character):
    def __init__(self, name, description, conversation, gift: None):
        super().__init__(name, description=description, conversation=conversation)
        self.gifts: List[Item] = gift or None

    def talk(self):
        if self.conversation:
            for n, line in enumerate(self.conversation.splitlines()):
                if n == 0:
                    print(f"[{self.name} says] {line}")
                else:
                    print(f"{' ' * (len(self.name) + 8)}{line}")

        if self.gifts:
            gift = self.gifts.pop()
            print(f"Dear friend, here is a gift for you...")
            print(f"{gift.name} is given to you")
            return gift



