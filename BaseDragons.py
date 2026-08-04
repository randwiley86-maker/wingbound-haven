"""
dragon.py
Wingbound Alliance

Contains the Dragon class and all dragon-related logic.
"""

from dataclasses import dataclass, field
from typing import List, Dict
import random


# -----------------------------
# Base Stats
# -----------------------------

@dataclass
class Stats:
    hp: int
    attack: int
    defense: int
    magic: int
    magic_defense: int
    speed: int
    spirit: int


# -----------------------------
# Dragon
# -----------------------------

@dataclass
class Dragon:

    species: str
    name: str

    level: int = 1
    experience: int = 0

    friendship: int = 0
    bond: int = 0

    egg_group: str = "Common"

    stats: Stats = field(default_factory=lambda:
        Stats(
            hp=50,
            attack=10,
            defense=10,
            magic=10,
            magic_defense=10,
            speed=10,
            spirit=10
        )
    )

    current_hp: int = 50

    corrupted: bool = False
    shiny: bool = False

    personality: str = "Calm"

    moves: List[str] = field(default_factory=list)

    equipment: List[str] = field(default_factory=list)

    status_effects: List[str] = field(default_factory=list)

    # -------------------------
    # Basic
    # -------------------------

    def is_alive(self):

        return self.current_hp > 0


    def heal(self, amount):

        self.current_hp += amount

        if self.current_hp > self.stats.hp:

            self.current_hp = self.stats.hp


    def full_heal(self):

        self.current_hp = self.stats.hp

        self.status_effects.clear()


    def take_damage(self, amount):

        damage = max(1, amount - self.stats.defense)

        self.current_hp -= damage

        if self.current_hp < 0:

            self.current_hp = 0

        return damage


    # -------------------------
    # Experience
    # -------------------------

    def experience_needed(self):

        return self.level * 100


    def gain_experience(self, amount):

        self.experience += amount

        while self.experience >= self.experience_needed():

            self.experience -= self.experience_needed()

            self.level_up()


    # -------------------------
    # Level Up
    # -------------------------

    def level_up(self):

        self.level += 1

        hp_gain = random.randint(3,6)
        atk_gain = random.randint(1,3)
        def_gain = random.randint(1,3)
        mag_gain = random.randint(1,3)
        mdef_gain = random.randint(1,3)
        spd_gain = random.randint(1,2)
        spr_gain = random.randint(1,2)

        self.stats.hp += hp_gain
        self.stats.attack += atk_gain
        self.stats.defense += def_gain
        self.stats.magic += mag_gain
        self.stats.magic_defense += mdef_gain
        self.stats.speed += spd_gain
        self.stats.spirit += spr_gain

        self.current_hp = self.stats.hp

        print(f"{self.name} reached Level {self.level}!")

        print(f"+{hp_gain} HP")
        print(f"+{atk_gain} Attack")
        print(f"+{def_gain} Defense")
        print(f"+{mag_gain} Magic")
        print(f"+{mdef_gain} Magic Defense")
        print(f"+{spd_gain} Speed")
        print(f"+{spr_gain} Spirit")


    # -------------------------
    # Friendship
    # -------------------------

    def add_friendship(self, amount):

        self.friendship += amount

        if self.friendship > 100:

            self.friendship = 100

        self.update_bond()


    def remove_friendship(self, amount):

        self.friendship -= amount

        if self.friendship < 0:

            self.friendship = 0

        self.update_bond()


    def update_bond(self):

        self.bond = self.friendship


    # -------------------------
    # Status
    # -------------------------

    def apply_status(self, status):

        if status not in self.status_effects:

            self.status_effects.append(status)


    def remove_status(self, status):

        if status in self.status_effects:

            self.status_effects.remove(status)


    # -------------------------
    # Moves
    # -------------------------

    def learn_move(self, move):

        if move not in self.moves:

            self.moves.append(move)


    def forget_move(self, move):

        if move in self.moves:

            self.moves.remove(move)


    # -------------------------
    # Save
    # -------------------------

    def to_dict(self):

        return {

            "species": self.species,

            "name": self.name,

            "level": self.level,

            "experience": self.experience,

            "friendship": self.friendship,

            "bond": self.bond,

            "egg_group": self.egg_group,

            "current_hp": self.current_hp,

            "corrupted": self.corrupted,

            "shiny": self.shiny,

            "personality": self.personality,

            "moves": self.moves,

            "equipment": self.equipment,

            "status_effects": self.status_effects,

            "stats": vars(self.stats)

        }
