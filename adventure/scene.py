from typing import List
from dataclasses import dataclass
from adventure.room import Room
from adventure.challenge import Challenge
from adventure.item import Item


@dataclass
class Scene:
    challenges: List[Challenge]
    room: Room
    level: int
    score: int
    health: int
    backpack: List[Item]
    level_up_points: int
    help: str
    welcome_msg: str
    gameover_msg: str
    endgame_msg: str

    # for classmethod
    author: str = "Jeremy Chen"

    def __init__(
        self,
        room,
        level=0,
        score=0,
        health=3,
        backpack=None,
        level_up_points=3,
        help_="help",
    ):
        self.room = room
        self.level = level
        self.score = score
        self.health = health
        self.backpack = backpack or []
        self.level_up_points = level_up_points
        self.help = help_

    def welcome(self):
        print(self.welcome_msg)

    def endgame(self):
        print(self.endgame_msg)
        self.credits()

    def gameover(self):
        print(self.gameover_msg)
        self.credits()

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print(f"\nMade by {cls.author}")
