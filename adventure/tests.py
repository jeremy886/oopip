import pytest
from adventure.room import Room, Furniture
from adventure.item import Item, Capable
from adventure.character import Character, Enemy, Friend
from adventure.command import Command
from adventure.scene import Scene
from adventure.main import main


@pytest.fixture
def scene_2_sn_rooms():
    room_n = Room("Kitchen")
    room_s = Room("Toilet")
    room_n.link_room(room_s, "south")
    scene = Scene(room=room_n, level_up_points=3)
    command = Command(scene)
    return room_n, room_s, scene, command

def test_create_rooms(capsys):
    kitchen = Room("Kitchen")
    kitchen.name = "Old kitchen"
    kitchen.description = "A dank and dirty place, buzzing with flies"
    kitchen.describe()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Old Kitchen: A dank and dirty place, buzzing with flies"


def test_linked_rooms():
    kitchen = Room("Kitchen")
    toilet = Room("Toilet")
    kitchen.link_room(toilet, "south")
    assert kitchen.linked_rooms["south"] is toilet


def test_create_items(capsys):
    sword = Item("Silver Sword", "a heavy sword that can cut any level 1 monsters", Capable.FIGHT)
    sword.describe()
    captured = capsys.readouterr()
    assert  captured.out.strip() == "* Silver Sword: a heavy sword that can cut any level 1 monsters"


def test_create_characters(capsys):
    dave = Character("Dave", "a zombie has a strong smell but looks friendly")
    dave.conversation = "Do you want to have a bite?"
    dave.describe()
    captured = capsys.readouterr()
    assert captured.out.strip() == "@ Dave is here!\n  a zombie has a strong smell but looks friendly"
    dave.talk()
    captured = capsys.readouterr()
    assert captured.out.strip() == "[Dave says] Do you want to have a bite?"


# def test_character_multiline_talk(monkeypatch, capsys):
#     from io import StringIO
#     monkeypatch.setattr("sys.stdin", StringIO("\n"))
#
#     dave = Character("Dave")
#     dave.conversation = "If you want to know where to go, you can ask me.\nMany people did that."
#     captured = capsys.readouterr()
#     dave.talk()
#     assert captured.out.strip() == "If you want to know where to go, you can ask me.\nMany people did that."


def test_character_no_talk(capsys):
    dave = Character("Dave", "a zombie has a strong smell but looks friendly")
    dave.conversation = ""
    dave.talk()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Dave doesn't want to talk to you"


def test_character_talk(capsys):
    dave = Character("Dave", "a zombie has a strong smell but looks friendly")
    dave.conversation = "Do you want to have a bite?"
    dave.talk()
    captured = capsys.readouterr()
    assert captured.out.strip() == "[Dave says] Do you want to have a bite?"


def test_character_multipline_talk():
    dave = Character("Dave")
    dave.conversation = "If you want to know more, ask me.\nMany people did that."
    assert dave.conversation == "If you want to know more, ask me.\nMany people did that."


def test_create_enemy(capsys):
    dave = Enemy(name="Dave")
    dave.describe()
    captured = capsys.readouterr()
    assert captured.out.strip() == "@ Dave is here!\n  a smelly zombie"

    tim = Enemy(name="Tim")
    tim.describe()
    captured = capsys.readouterr()
    assert captured.out.strip() == "@ Tim is here!\n  a smelly zombie"


# Commands Group
def test_user_choice_1_character(scene_2_sn_rooms):
    room_n, room_s, scene, command = scene_2_sn_rooms
    dave = Character("Dave", "a zombie has a strong smell but looks friendly")
    room_n.characters.append(dave)
    assert command.choose_obj(room_n.characters) == dave

def test_user_choice_2_characters(scene_2_sn_rooms, monkeypatch):
    room_n, room_s, scene, command = scene_2_sn_rooms
    dave = Character("Dave", "a zombie has a strong smell but looks friendly")
    room_n.characters.append(dave)
    don = Character("Don", "a zombie looked very scary")
    room_n.characters.append(don)
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert command.choose_obj(room_n.characters) == don
    monkeypatch.setattr("builtins.input", lambda _: "0")
    assert command.choose_obj(room_n.characters) == dave

def test_user_input_shortcuts(scene_2_sn_rooms):
    room_n, room_s, scene, command = scene_2_sn_rooms
    for action in "ewnstflhipgu":
        assert action in command.commands.keys()




def test_user_input_shortcut_south_north(scene_2_sn_rooms):

    room_n, room_s, scene, command = scene_2_sn_rooms
    # direction
    room0 = scene.room  # kitchen

    command.exec("s")
    room1 = scene.room  # toilet

    command.exec("n")
    room2 = scene.room  # kitchen

    command.exec("south")
    room3 = scene.room  # toilet

    command.exec("north")
    room4 = scene.room  # kitchen

    assert room3.name == "Toilet"
    assert room0.name == room2.name
    assert room1.name == room3.name
    assert room0.name == room4.name


def test_input_t_only_for_talk_not_fight(scene_2_sn_rooms, capsys):
    room_n, room_s, scene, command = scene_2_sn_rooms
    command.exec("t")
    captured1 = capsys.readouterr()
    command.exec("talk")
    captured2 = capsys.readouterr()
    assert captured1.out == captured2.out

def test_user_input_shortcut_south_north(scene_2_sn_rooms, capsys):
    pass
    room_n, room_s, scene, command = scene_2_sn_rooms
    shortcut = command.exec("t")
    captured = capsys.readouterr()
    normal = command.exec("talk")
    # assert shortcut == ""
    #assert  captured.out.strip() == "Silver Sword: a heavy sword that can cut any level 1 monsters"
    #assert shortcut == normal

# Comment
    # room_n, room_s, scene, command = scene_2_sn_rooms
    #capsys.readouterr()
    #monkeypatch.setattr("builtins.input", lambda _: "\n")
    #captured = capsys.readouterr()
    #assert captured.out == "< you don't have enough scores to level up"

def test_create_furniture_with_items_in_room():
    room = Room("Kitchen")
    assert room.items == []
    chair = Furniture("Chair", "A high chair with only one very think glass leg")
    assert chair.name == "Chair"
    item1 = Item("Gem", "a pretty green gem stone")
    item2 = Item("Gold nugget", "as big as an chicken egg but golden and shiny")
    chair.items.append(item1)
    chair.items.append(item2)
    assert chair.items == [item1, item2]
    room.items.append(chair.probe())
    assert room.items[0] in set((item1, item2))
    room.items.append(chair.probe())
    assert sorted(room.items, key=id) == sorted([item1, item2], key=id)


def test_grab_items_from_room():
    room = Room("Kitchen")
    item1 = Item("Gem", "a pretty green gem stone")
    item2 = Item("Gold nugget", "as big as an chicken egg but golden and shiny")
    room.items.append(item1)
    room.items.append(item2)


# talk and gift

def test_talk_to_friend_get_gift():
    jim = Friend(
        name="Jim",
        description="a flying elephant",
        conversation="You get 1 score after killing an enemy"
        + "\nYou need 3 points to level up...",
        gift=[Item("Key")],
    )
    assert jim.talk().name == "Key"


def test_talk_to_friend_get_gift():
    jim = Friend(
        name="Jim",
        description="a flying elephant",
        conversation="You get 1 score after killing an enemy"
        + "\nYou need 3 points to level up...",
        gift=[],
    )
    assert jim.talk() is None


# def test_add_remove_item_to_room():
#
#     room.items.append()
#     item1 = Item("Gem", "a pretty green gem stone")


# Game Loop

def test_level_up(capsys, monkeypatch):
    # manual test
    pass

