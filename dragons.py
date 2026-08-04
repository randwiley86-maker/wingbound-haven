"""
species.py
Wingbound Alliance

Defines all dragon species and how to create them.
"""

from dragon import Dragon, Stats

# -----------------------------
# Species Database
# -----------------------------

SPECIES = {

    "Star Dragon": {
        "egg_group": "Celestial",
        "stats": Stats(
            hp=70,
            attack=18,
            defense=15,
            magic=24,
            magic_defense=20,
            speed=22,
            spirit=30
        ),
        "moves": [
            "Comet Dash",
            "Starlight Aegis"
        ]
    },

    "Forest Dragon": {
        "egg_group": "Nature",
        "stats": Stats(
            hp=80,
            attack=16,
            defense=18,
            magic=12,
            magic_defense=16,
            speed=15,
            spirit=18
        ),
        "moves": [
            "Leaf Slash",
            "Nature's Blessing"
        ]
    },

    "Fire Dragon": {
        "egg_group": "Elemental",
        "stats": Stats(
            hp=72,
            attack=25,
            defense=14,
            magic=18,
            magic_defense=12,
            speed=20,
            spirit=12
        ),
        "moves": [
            "Fire Breath",
            "Flame Burst"
        ]
    },

    "Sky Dragon": {
        "egg_group": "Wind",
        "stats": Stats(
            hp=65,
            attack=18,
            defense=14,
            magic=20,
            magic_defense=18,
            speed=30,
            spirit=20
        ),
        "moves": [
            "Gust Wing",
            "Sky Dive"
        ]
    },

    "Crystal Dragon": {
        "egg_group": "Crystal",
        "stats": Stats(
            hp=90,
            attack=15,
            defense=28,
            magic=18,
            magic_defense=24,
            speed=10,
            spirit=20
        ),
        "moves": [
            "Crystal Spike",
            "Crystal Shield"
        ]
    },

    "Shadow Dragon": {
        "egg_group": "Shadow",
        "stats": Stats(
            hp=75,
            attack=22,
            defense=16,
            magic=28,
            magic_defense=18,
            speed=18,
            spirit=8
        ),
        "moves": [
            "Shadow Claw",
            "Dark Pulse"
        ]
    }

}

# -----------------------------
# Create Dragon
# -----------------------------

def create_dragon(species_name, nickname=None):

    if species_name not in SPECIES:
        raise ValueError(f"Unknown species: {species_name}")

    data = SPECIES[species_name]

    dragon = Dragon(
        species=species_name,
        name=nickname or species_name
    )

    dragon.stats = Stats(
        hp=data["stats"].hp,
        attack=data["stats"].attack,
        defense=data["stats"].defense,
        magic=data["stats"].magic,
        magic_defense=data["stats"].magic_defense,
        speed=data["stats"].speed,
        spirit=data["stats"].spirit
    )

    dragon.current_hp = dragon.stats.hp
    dragon.egg_group = data["egg_group"]

    for move in data["moves"]:
        dragon.learn_move(move)

    return dragon
