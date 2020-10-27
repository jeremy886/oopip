from typing import List
from dataclasses import dataclass
from enum import Enum, auto


class Difficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


@dataclass
class Challenge:
    quiz: str
    ans: List[str]
    difficulty: Difficulty

    def __init__(self, quiz="1+1=? ", ans=None, difficulty=Difficulty.EASY):
        self.quiz = quiz
        self.ans = ans or ["2"]
        self.difficulty = difficulty
