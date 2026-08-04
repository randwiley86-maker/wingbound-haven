"""
world.py
Wingbound Alliance

Controls:
- Maps
- Exploration
- Weather
- Time
- Wild Dragon Spawning
- Resources
- Eggs
"""

import random


# ============================================
# Time System
# ============================================

TIMES_OF_DAY = [
    "Morning",
    "Day",
    "Evening",
    "Night"
]


class TimeSystem:

    def __init__(self):

        self.day = 1
        self.time_index = 0

    @property
    def current_time(self):

        return TIMES_OF_DAY[self.time_index]

    def advance(self):

        self.time_index += 1

        if self.time_index >= len(TIMES_OF_DAY):

            self.time_index = 0
            self.day += 1

        print(f"It is now {self.current_time} (Day {self.day})")


# ============================================
# Weather
# ============================================

WEATHER_TYPES = [

    "Sunny",

    "Cloudy",

    "Rain",

    "Storm",

    "Fog",

    "Snow"

]


class WeatherSystem:

    def __init__(self):

        self.weather = random.choice(WEATHER_TYPES)

    def next_weather(self):

        self.weather = random.choice(WEATHER_TYPES)

        print("Weather changed to:", self.weather)


# ============================================
# Resource Database
# ============================================

RESOURCE_TABLE = {

    "Whisper Forest":[

        "Berry",

        "Herb",

        "Dragon Feather"

    ],

    "Blooming Vale":[

        "Flower",

        "Berry",

        "Ancient Seed"

    ],

    "Crystal Caverns":[

        "Crystal Shard",

        "Ancient Crystal"

    ],

    "Frost Peaks":[

        "Ice Crystal",

        "Frozen Herb"

    ]

}


# ============================================
# Egg Database
# ============================================

EGG_TABLE = {

    "Whisper Forest":[

        "Forest Egg"

    ],

    "Blooming Vale":[

        "Nature Egg"

    ],

    "Crystal Caverns":[

        "Crystal Egg"

    ],

    "Frost Peaks":[

        "Frost Egg"

    ]

}


# ============================================
# Dragon Spawn Tables
# ============================================

DRAGON_SPAWNS = {

    "Whisper Forest":[

        ("Forest Dragon",60),

        ("Sky Dragon",20),

        ("Moss Dragon",15),

        ("Star Dragon",5)

    ],

    "Blooming Vale":[

        ("Forest Dragon",40),

        ("Sky Dragon",30),

        ("Crystal Dragon",20),

        ("Star Dragon",10)

    ],

    "Crystal Caverns":[

        ("Crystal Dragon",70),

        ("Shadow Dragon",15),

        ("Mountain Dragon",15)

    ],

    "Frost Peaks":[

        ("Frost Dragon",60),

        ("Mountain Dragon",25),

        ("Sky Dragon",15)

    ]

}


# ============================================
# Area Class
# ============================================

class Area:

    def __init__(

        self,

        name,

        description

    ):

        self.name = name

        self.description = description

    def enter(self):

        print()

        print("==========")

        print(self.name)

        print("==========")

        print(self.description)

        print()


# ============================================
# World
# ============================================

class World:

    def __init__(self):

        self.time = TimeSystem()

        self.weather = WeatherSystem()

        self.current_area = "Wingbound City"

        self.areas = {

            "Wingbound City":

            Area(

                "Wingbound City",

                "The home of the Wingbound Alliance."

            ),

            "Whisper Forest":

            Area(

                "Whisper Forest",

                "Ancient trees whisper in the wind."

            ),

            "Blooming Vale":

            Area(

                "Blooming Vale",

                "A peaceful valley filled with flowers."

            ),

            "Crystal Caverns":

            Area(

                "Crystal Caverns",

                "Glittering caves beneath the mountains."

            ),

            "Frost Peaks":

            Area(

                "Frost Peaks",

                "Cold snowy mountains."

            )

        }

    # -----------------------

    # Travel

    # -----------------------

    def travel(self, destination):

        if destination not in self.areas:

            print("Unknown area.")

            return

        self.current_area = destination

        self.time.advance()

        self.weather.next_weather()

        self.areas[destination].enter()

    # -----------------------

    # Explore

    # -----------------------

    def explore(self):

        print()

        print("Exploring", self.current_area)

        print("Time:", self.time.current_time)

        print("Weather:", self.weather.weather)

        print()

        roll = random.randint(1,100)

        if roll <= 50:

            self.find_resource()

        elif roll <= 80:

            self.find_dragon()

        elif roll <= 90:

            self.find_egg()

        else:

            print("Nothing interesting happened.")

    # -----------------------

    # Resource

    # -----------------------

    def find_resource(self):

        if self.current_area not in RESOURCE_TABLE:

            print("No resources here.")

            return

        item = random.choice(

            RESOURCE_TABLE[self.current_area]

        )

        print("You found:", item)

    # -----------------------

    # Egg

    # -----------------------

    def find_egg(self):

        if self.current_area not in EGG_TABLE:

            print("No eggs here.")

            return

        egg = random.choice(

            EGG_TABLE[self.current_area]

        )

        print("You discovered a", egg)

    # -----------------------

    # Dragon

    # -----------------------

    def find_dragon(self):

        if self.current_area not in DRAGON_SPAWNS:

            print("No dragons appear here.")

            return

        table = DRAGON_SPAWNS[self.current_area]

        roll = random.randint(1,100)

        total = 0

        for dragon, chance in table:

            total += chance

            if roll <= total:

                print("A wild", dragon, "appeared!")

                return
# ============================================
# NPC System
# ============================================

class NPC:

    def __init__(self, name, job, dialogue):

        self.name = name
        self.job = job
        self.dialogue = dialogue

    def talk(self):

        print()
        print(self.name)
        print("(" + self.job + ")")
        print(self.dialogue)
        print()


NPCS = {

    "Wingbound City":[

        NPC(
            "Elder Rowan",
            "Council Leader",
            "The Wingbound Alliance grows stronger every day."
        ),

        NPC(
            "Luna",
            "Dragon Caretaker",
            "Treat dragons with kindness and they'll trust you."
        ),

        NPC(
            "Finn",
            "Merchant",
            "I've got supplies if you've got coins!"
        )

    ],

    "Blooming Vale":[

        NPC(
            "Willow",
            "Researcher",
            "I study dragon friendships."
        )

    ],

    "Whisper Forest":[

        NPC(
            "Oak",
            "Explorer",
            "I swear I saw a Star Dragon last night..."
        )

    ]

}


# ============================================
# Treasure Chests
# ============================================

TREASURE_TABLE = {

    "Whisper Forest":[

        "50 Coins",
        "Healing Herb",
        "Forest Gem"

    ],

    "Crystal Caverns":[

        "Crystal Core",
        "Rare Crystal",
        "200 Coins"

    ],

    "Frost Peaks":[

        "Ice Gem",
        "Warm Cloak"

    ]

}


# ============================================
# Corruption Zones
# ============================================

CORRUPTION_ZONES = {

    "Shadow Portal":5,

    "Dark Forest":3

}


# ============================================
# Random Events
# ============================================

WORLD_EVENTS = [

    "A shooting star flies overhead.",

    "Alice suddenly becomes alert.",

    "You hear distant dragon calls.",

    "A cool breeze blows through the area.",

    "You discover old dragon footprints.",

    "A rainbow appears."

]


# ============================================
# Quests
# ============================================

QUESTS = [

    "Help a lost hatchling.",

    "Gather 5 Herbs.",

    "Defeat a corrupted dragon.",

    "Find an Ancient Crystal.",

    "Deliver supplies to Wingbound City."

]


# ============================================
# Add functions to World
# ============================================

def talk_to_random_npc(world):

    area = world.current_area

    if area not in NPCS:

        print("Nobody is nearby.")
        return

    npc = random.choice(NPCS[area])

    npc.talk()


def open_treasure(world):

    area = world.current_area

    if area not in TREASURE_TABLE:

        print("No treasure nearby.")
        return

    reward = random.choice(TREASURE_TABLE[area])

    print("You opened a treasure chest!")
    print("Found:", reward)


def random_world_event():

    print()
    print(random.choice(WORLD_EVENTS))
    print()


def random_quest():

    print()
    print("New Quest!")
    print(random.choice(QUESTS))
    print()


def corruption_level(world):

    area = world.current_area

    if area not in CORRUPTION_ZONES:

        print("This area is peaceful.")
        return

    print(
        "Corruption Level:",
        CORRUPTION_ZONES[area],
        "/10"
    )
