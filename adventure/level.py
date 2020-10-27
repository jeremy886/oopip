from random import shuffle
from adventure.room import Room, Furniture
from adventure.item import Item, Capable
from adventure.character import Character, Enemy, Friend
from adventure.command import Command
from adventure.scene import Scene
from adventure.challenge import Challenge, Difficulty


def build_level_0():
    # make challenges
    challenges = [
        Challenge(
            quiz="1+1=?",
            ans=["2"],
            difficulty=Difficulty.EASY,
        ),
        Challenge(
            quiz="In the number 123, what is the place value of the digit 2",
            ans=["10", "ten"],
            difficulty=Difficulty.MEDIUM,
        ),
        Challenge(
            quiz="If you put 5*5 into your calculator or python, you will get",
            ans=["25", "twenty-five", "twenty five"],
            difficulty=Difficulty.MEDIUM,
        ),
        Challenge(
            quiz="In BIDMAS, what is B?",
            ans=["bracket", "brackets"],
            difficulty=Difficulty.HARD,
        ),
    ]
    shuffle(challenges)

    # build rooms
    kitchen = Room("Old kitchen")
    kitchen.description = "A dank and dirty place, buzzing with flies"
    ballroom = Room("Dark ballroom")
    ballroom.description = "Teeny music coming out of nowhere in the dark"
    dining_hall = Room("Dining Hall")
    dining_hall.description = "Candles, hundreds of them, floating in the air"
    kitchen.link_room(dining_hall, "south")
    dining_hall.link_room(ballroom, "west")

    # arrange furniture
    table = Furniture("Marble table", "1000 year-old ancient table")

    map = Item("Map", "show you rooms in this level", Capable.READ)
    map.usage = """
░░░░░░░░░░░░░░░░┌─────────────┐
░░░░░░░░░░░░░░░░│░░░░░░░░░░░░░│
░░░░░N░░░░░░░░░░│░░░░░░░░░░░░░│
░░░░░│░░░░░░░░░░│░░Kitchen░░░░│
░░░░░│░░░░░░░░░░│░░░░░░░░░░░░░│
░░░░░S░░░░░░░░░░│░░░░░░░░░░░░░│
░░░░░░░░░░░░░░░░│░░░░░░░░░░░░░│
┌───────────────┼────═════────┤
│░░░░░░░░░░░░░░░│░░░░░░░░░░░░░│
│░░░░░░░░░░░░░░░│░░░░░░░░░░░░░│
│░░░░Ballroom░░░║░░Dining░░░░░│
│░░░░░░░░░░░░░░░║░░Hall░░░░░░░│
│░░░░░░░░░░░░░░░║░░░░░░░░░░░░░│
│░░░░░░░░░░░░░░░│░░░░░░░░░░░░░│
└───────────────┴─────────────┘
"""
    table.items.append(map)
    kitchen.furnitures.append(table)

    # create characters
    joe = Character(
        name="Joe",
        conversation=f"This is level 0. There are rooms to explore"
        + "\nUse e s w n to move around"
        + "\nType ^ to up a level when you score high enough"
        + "\nNow use s to go south...",
    )
    john = Character(
        name="John", conversation="Kill all zombies to go to next level..."
    )
    jim = Friend(
        name="Jim",
        description="a flying elephant",
        conversation="You get 1 score after killing an enemy"
        + "\nYou need 3 points to level up...",
        gift=[Item("Key")],
    )
    dave = Enemy(name="Dave", challenge=challenges.pop())
    dave.conversation = "I am ready to fight you"
    dean = Enemy(name="Dean", conversation="Fight me!", challenge=challenges.pop())
    don = Enemy(
        name="Don",
        description="Very smelly zombie",
        conversation="Fight me to score a point",
        challenge=challenges.pop(),
    )

    # add characters to rooms
    kitchen.characters.append(joe)
    dining_hall.characters.append(dave)
    dining_hall.characters.append(dean)
    dining_hall.characters.append(john)
    ballroom.characters.append(jim)
    ballroom.characters.append(don)

    scene = Scene(room=kitchen, level_up_points=3)
    command = Command(scene)
    scene.help = """
    =============================================================
    Use E to go EAST, W to go WEST, N to go NORTH, S to go SOUTH.
    Use T to talk and L to look around.
    Use F to fight and U to use items.
    Use P to probe furniture and G to grab items.
    Use I to check items in your backpack.
    Use H to see this help menu again.
    =============================================================
    """
    scene.welcome_msg = r"""
    You cannot escape the Equation Zombie HOUSE
                           \                     
                                .....            
                               C C  /            
                              /<   /             
               ___ __________/_#__=o             
              /(- /(\_\________   \              
              \ ) \ )_      \o     \             
              /|\ /|\       |'     |             
                            |     _|             
                            /o   __\             
                           / '     |             
                          / /      |             
                         /_/\______|             
                        (   _(    <              
                         \    \    \             
                          \    \    |            
                           \____\____\           
                           ____\_\__\_\          
                         /`   /`     o\          
                         |___ |_______|.. . b'ger
"""
    scene.endgame_msg = "You have completed the adventure!"
    scene.gameover_msg = "You've lost the game and your brain."

    scene.welcome()
    command.help()
    scene.room.info()
    return scene, command


def build_level_1():
    # level data from https://www.thievesguild.cc/generators/dungeon-room-generator
    # make challenges
    challenges = [
        Challenge(
            quiz="Find the pronumeral in:\n2p+1",
            ans=["p"],
            difficulty=Difficulty.EASY,
        ),
        Challenge(
            quiz='Use the language of algebra to describe "3d"',
            ans=["term"],
            difficulty=Difficulty.HARD,
        ),
        Challenge(
            quiz="Which one is a constant (number)?\na. 3*x\nb. 1.1\nc. 2x\nd. 2+x",
            ans=["b"],
            difficulty=Difficulty.EASY,
        ),
        Challenge(
            quiz="Show me the coefficient of -5y",
            ans=["-5"],
            difficulty=Difficulty.MEDIUM,
        ),
        Challenge(
            quiz="Find the like terms in: -b + 3a + b - 2\na. a and b\nb.-b and -2\nc. -1 and 1 \nd. -b and b",
            ans=["d"],
            difficulty=Difficulty.HARD,
        ),
        Challenge(
            quiz='Make an expression with variable "m" and a constant "3"\na. 3m\nb. -m-33\nc. 3-3m\nd. m3',
            ans=["c"],
            difficulty=Difficulty.HARD,
        ),
        Challenge(
            quiz='What does "2xy" mean?\na. 2+y+y\nb. 2*100+10*x+y\nc. 200 to 299\nd. 2*x*y',
            ans=["d"],
            difficulty=Difficulty.EASY,
        ),
        Challenge(
            quiz='How to express "a unknown number is divided by 3" in Algebra?\na. x/3\nb. 5/3\nc. n.3\nd. a div 3',
            ans=["a"],
            difficulty=Difficulty.MEDIUM,
        ),
        Challenge(
            quiz="Find the equivalent expression of: 2b + 3 + 2 - b\na. 2b+10\nb. 5\nc. b+5\nd. 5b",
            ans=["c"],
            difficulty=Difficulty.HARD,
        ),
        Challenge(
            quiz="If a is 3, find the value of 5 - a",
            ans=["2"],
            difficulty=Difficulty.EASY,
        ),
        Challenge(
            quiz="If y is 2, find the value of 10 - 7y",
            ans=["-4"],
            difficulty=Difficulty.HARD,
        ),
        Challenge(
            quiz="Find the value of this expression (5-3)*10+5",
            ans=["25"],
            difficulty=Difficulty.EASY,
        ),
    ]
    shuffle(challenges)

    # build rooms

    birdhouse = Room(
        "Birdhouse",
        "A chill crawls up your spine and out over your skin as you look upon this room",
    )
    bathroom = Room(
        "Bathroom", "Scenes of death, both violent and peaceful, appear on every wall"
    )
    lounge = Room(
        "Lounge",
        "A chill wind blows against you as you open the door. Beyond it, you see that the floor and ceiling are nothing but iron grates.",
    )
    gym = Room("Gym", "You hear a low rumbling and cracking noise")
    bedroom = Room(
        "Bedroom", "Rotting corpses on the beds and the unclean cages everywhere"
    )
    kitchen = Room(
        "Kitchen",
        "The door creaks open, which somewhat overshadows the sound of bubbling liquid",
    )
    laundry = Room(
        "Laundry",
        "Three tables bend beneath a clutter of bottles of liquid and connected glass piping",
    )
    masterroom = Room(
        "Master room",
        "Several white marble busts that rest on white pillars dominate this room",
    )
    sunroom = Room(
        "Sunroom",
        "A pungent, earthy odor greets you and mushrooms grow in clusters of hundreds all over the floor.",
    )
    birdhouse.link_room(bathroom, "west")
    bathroom.link_room(lounge, "west")
    lounge.link_room(gym, "north")
    gym.link_room(bedroom, "north")
    bedroom.link_room(kitchen, "east")
    kitchen.link_room(laundry, "east")
    laundry.link_room(masterroom, "south")
    masterroom.link_room(sunroom, "east")

    # arrange furniture
    cage = Furniture("Bird cages", "Only dead birds inside")
    mirror = Furniture("Mirror", "Red stains on the broken mirror")
    sofa = Furniture("New sofa", "A brand new soft in an old house")
    bike = Furniture("Bike", "a rusty bike")
    dumbbell = Furniture("Dumbbells", "Made out of bones and skulls")
    cauldron = Furniture("Cauldron", "Green liquid and smoke come out of it")
    teapot = Furniture("A small teapot", "A beautifully shaped Japanese teapot")
    sunflower = Furniture("Human face sunflower", "Stick out its bloody tongue")

    birdhouse.furnitures.append(cage)
    bathroom.furnitures.append(mirror)
    lounge.furnitures.append(sofa)
    gym.furnitures.append(bike)
    gym.furnitures.append(dumbbell)
    kitchen.furnitures.append(cauldron)
    kitchen.furnitures.append(teapot)
    sunroom.furnitures.append(sunflower)

    # items
    map = Item("Map", "show you rooms in this level", Capable.READ)
    map.usage = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░N░░░░░░░░█████████████░░░░░░░░░░░░░
░░|░░░░░░░░█░Kitchen░░░█░░░░░░░░░░░░░
░░|░░░░░░░░█░░░░░░░░░░░█░░░░░░░░░░░░░
░░S░░░░░░░░█░░░░░░░░░░░███████░░░░░░░
░░░░████████░░░░░░░░░░░█Laundry░░░░░░
░░░░█░░░░░║║░░░░░░░░░░░║░░░░░█░░░░░░░
░░░░█Bed░░█████████████████══█████░░░
░░░░█░room█░░░░░░░░░░░░█░░░░░░░░░█░░░
░░░░█░░░░░█░░░░░░░░░░░░█░Master░░█░░░
░░░░█░░░░░█░░░░░░░░░░░░█░Room░░░░█░░░
██████══████████░░░░░░░█░░░░░░░██████
██░░░░░░░░░░░░░█░░░░░░░█░░░░░░░║░░░░█
██░░░░░Gym░░░░░█░░░░░░░█████████░Sun█
██░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█Room█
████░░░░░░░░████░░░░░░░░░░░░░░░██████
░░░████══████░░░░░░░░░░██████████░░░░
░░░██░░░░░░██░░░░░░░░░░██░Bird░██░░░░
░░░██Lounge██████████████House░██░░░░
░░░██░░░░░░██░Bathroom░██░░░░░░██░░░░
░░░██░░░░░░║║░░░░░░░░░░║║░░░░░░██░░░░
░░░██░░░░░░██████████████████████░░░░
░░░██░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░
░░░██████████░░░░░░░░░░░░░░░░░░░░░░░░
"""
    mirror.items.append(map)
    key = Item("Key")
    dumbbell.items.append(key)

    # create characters
    joe = Character(
        name="Joe",
        conversation=f"This is level 1. There are many dangerous rooms to explore",
    )
    john = Character(name="John", conversation="Kill zombies to go to next level...")
    jarred = Character(
        name="Jarred", conversation="I like to ride a bike...the map is in the bathroom"
    )
    jim = Friend(
        name="Jim",
        description="a flying piggy",
        conversation="You get 1 score after killing an enemy"
        + "\nYou need 8 points to level up...",
        gift=[Item("Carrot Cake", "Yummy", Capable.FOOD)],
    )

    dave = Enemy(
        "Dave", "A small zombie", "Your brain looks very tasty", challenges.pop()
    )
    dean = Enemy(
        "Dean",
        "A stinky green zombie",
        "Keep an arm and a leg before you go",
        challenges.pop(),
    )
    dan = Enemy(
        "Dan", "A fat old zombie", "I'm hungry. I need your blood", challenges.pop()
    )
    dex = Enemy(
        "Dex",
        "A skinny tall zombie",
        "I can't see you but I will eat you",
        challenges.pop(),
    )
    dale = Enemy("Dale", "A freshly dead zombie", "You are the next", challenges.pop())
    dash = Enemy(
        "Dash", "A gruesome hairless zombie", "Your head is mine", challenges.pop()
    )
    declan = Enemy(
        "Declan", "A transparent zombie", "You can't see me. Fear not", challenges.pop()
    )
    diana = Enemy(
        "Diana", "A happy zombie", "Good to see you! Dinner time", challenges.pop()
    )
    dawn = Enemy(
        "Dawn", "A coughing zombie", "Excuse me. Do you have tissue?", challenges.pop()
    )
    dara = Enemy("Dara", "A sleepy zombie", "Why do you wake me up?", challenges.pop())
    dior = Enemy(
        "Dior", "A powerful zombie", "Black magic is the key", challenges.pop()
    )
    dee = Enemy(
        "Dee", "A adorable zombie", "I'm on a small person diet", challenges.pop()
    )

    # add characters to rooms
    birdhouse.characters.append(joe)
    bathroom.characters.append(dave)
    bathroom.characters.append(dean)
    bathroom.characters.append(john)
    lounge.characters.append(dee)
    gym.characters.append(jarred)
    gym.characters.append(jim)
    gym.characters.append(dior)
    gym.characters.append(dara)
    gym.characters.append(dan)
    bedroom.characters.append(dawn)
    laundry.characters.append(diana)
    masterroom.characters.append(dex)
    masterroom.characters.append(dale)
    sunroom.characters.append(dash)
    sunroom.characters.append(declan)

    scene = Scene(room=birdhouse, level=1, health=5, level_up_points=8)
    command = Command(scene)
    scene.help = """
    =============================================================
    Use E to go EAST, W to go WEST, N to go NORTH, S to go SOUTH.
    Use T to talk and L to look around.
    Use F to fight and U to use items.
    Use P to probe furniture and G to grab items.
    Use I to check items in your backpack.
    Use H to see this help menu again.
    =============================================================
    """

    scene.welcome_msg = "Welcome to Level 1\nYou cannot escape the Equation Zombie HOUSE"
    scene.endgame_msg = "You have completed the adventure!"
    scene.gameover_msg = "You've lost the game and your brain."

    scene.welcome()
    command.help()
    scene.room.info()
    return scene, command
