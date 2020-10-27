from typing import Tuple

from adventure.level import build_level_0, build_level_1
from adventure.scene import Scene


def check_level_up_conditions(scene: Scene, level: int) -> Tuple[Scene, int]:
    # Todo: use set to check level up conditions
    if scene.score >= scene.level_up_points:
        if "Key" in [item.name.title() for item in scene.backpack]:
            level += 1
            scene.to_build_level = True
        else:
            print("< You get enough scores but you need a key to level up")
    else:
        print("< you don't have enough scores to level up")
    return scene, level


def build_level(ready_levels, level):
    scene, command = ready_levels[level]()
    scene.to_build_level = False
    return scene, command


def main():
    level = 0
    ready_levels = [build_level_0, build_level_1]
    scene, command = build_level(ready_levels, level)
    while True:
        if scene.to_build_level:
            if level >= len(ready_levels):
                scene.endgame()
                return
            else:
                scene, command = build_level(ready_levels, level)
        if scene.health <= 0:
            scene.gameover()
            return

        action = input(
            f"L:{scene.level} S:{scene.score} H:{scene.health} I:{len(scene.backpack)}> "
        ).lower()
        if action in command.commands:
            command.exec(action)
        elif action == "^":
            scene, level = check_level_up_conditions(scene, level)
        else:
            print("< Unknown action")


if __name__ == "__main__":
    main()
