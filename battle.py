"""
battle.py
Wingbound Alliance

Handles turn-based dragon battles.
"""

import random


class Battle:

    def __init__(self, player_dragon, enemy_dragon):

        self.player = player_dragon
        self.enemy = enemy_dragon

        self.turn = 1
        self.finished = False

    # ----------------------------
    # Start Battle
    # ----------------------------

    def start(self):

        print("\n========================")
        print(" BATTLE START!")
        print("========================\n")

        print(f"{self.enemy.name} appeared!")
        print(f"Go, {self.player.name}!")

    # ----------------------------
    # Turn Order
    # ----------------------------

    def player_goes_first(self):

        if self.player.stats.speed >= self.enemy.stats.speed:
            return True

        return False

    # ----------------------------
    # Damage Formula
    # ----------------------------

    def physical_damage(self, attacker, defender):

        damage = (
            attacker.stats.attack
            - defender.stats.defense // 2
            + random.randint(0, 4)
        )

        return max(1, damage)

    def magic_damage(self, attacker, defender):

        damage = (
            attacker.stats.magic
            - defender.stats.magic_defense // 2
            + random.randint(2, 6)
        )

        return max(1, damage)

    # ----------------------------
    # Physical Attack
    # ----------------------------

    def physical_attack(self, attacker, defender):

        damage = self.physical_damage(attacker, defender)

        defender.current_hp -= damage

        if defender.current_hp < 0:
            defender.current_hp = 0

        print(
            f"{attacker.name} attacked!"
        )

        print(
            f"{defender.name} took {damage} damage!"
        )

    # ----------------------------
    # Magic Attack
    # ----------------------------

    def magic_attack(self, attacker, defender):

        damage = self.magic_damage(attacker, defender)

        defender.current_hp -= damage

        if defender.current_hp < 0:
            defender.current_hp = 0

        print(
            f"{attacker.name} used magic!"
        )

        print(
            f"{defender.name} took {damage} damage!"
        )

    # ----------------------------
    # HP Display
    # ----------------------------

    def show_hp(self):

        print()

        print(
            f"{self.player.name}: "
            f"{self.player.current_hp}/{self.player.stats.hp}"
        )

        print(
            f"{self.enemy.name}: "
            f"{self.enemy.current_hp}/{self.enemy.stats.hp}"
        )

        print()

    # ----------------------------
    # Check Winner
    # ----------------------------

    def battle_over(self):

        if self.player.current_hp <= 0:

            print(
                f"{self.player.name} fainted!"
            )

            self.finished = True

            return True

        if self.enemy.current_hp <= 0:

            print(
                f"{self.enemy.name} was defeated!"
            )

            xp = self.enemy.level * 25

            print(
                f"{self.player.name} gained {xp} XP!"
            )

            self.player.gain_experience(xp)

            self.finished = True

            return True

        return False

    # ----------------------------
    # Enemy AI
    # ----------------------------

    def enemy_turn(self):

        attack = random.choice(
            [
                "physical",
                "magic"
            ]
        )

        if attack == "physical":

            self.physical_attack(
                self.enemy,
                self.player
            )

        else:

            self.magic_attack(
                self.enemy,
                self.player
            )

    # ----------------------------
    # One Battle Turn
    # ----------------------------

    def next_turn(self):

        if self.finished:
            return

        print(
            f"\n----- Turn {self.turn} -----"
        )

        self.show_hp()

        if self.player_goes_first():

            self.physical_attack(
                self.player,
                self.enemy
            )

            if self.battle_over():
                return

            self.enemy_turn()

            self.battle_over()

        else:

            self.enemy_turn()

            if self.battle_over():
                return

            self.physical_attack(
                self.player,
                self.enemy
            )

            self.battle_over()

        self.turn += 1
# ============================================
# Critical Hits
# ============================================

    def critical_hit(self):

        # 10% chance

        return random.randint(1,100) <= 10


# ============================================
# Dodge Chance
# ============================================

    def attack_hits(self, attacker, defender):

        dodge = max(
            5,
            min(35,
                defender.stats.speed - attacker.stats.speed + 10
            )
        )

        roll = random.randint(1,100)

        return roll > dodge


# ============================================
# Stronger Physical Attack
# ============================================

    def physical_attack(self, attacker, defender):

        if not self.attack_hits(attacker, defender):

            print(f"{attacker.name}'s attack missed!")
            return

        damage = self.physical_damage(attacker, defender)

        crit = False

        if self.critical_hit():

            damage *= 2
            crit = True

        defender.current_hp -= damage

        if defender.current_hp < 0:
            defender.current_hp = 0

        print(f"{attacker.name} attacked!")

        if crit:
            print("Critical Hit!")

        print(f"{defender.name} took {damage} damage!")


# ============================================
# Stronger Magic Attack
# ============================================

    def magic_attack(self, attacker, defender):

        if not self.attack_hits(attacker, defender):

            print(f"{attacker.name}'s spell missed!")
            return

        damage = self.magic_damage(attacker, defender)

        crit = False

        if self.critical_hit():

            damage *= 2
            crit = True

        defender.current_hp -= damage

        if defender.current_hp < 0:
            defender.current_hp = 0

        print(f"{attacker.name} used magic!")

        if crit:
            print("Critical Spell!")

        print(f"{defender.name} took {damage} damage!")


# ============================================
# Status Effects
# ============================================

    def apply_status_effects(self, dragon):

        if "Burn" in dragon.status_effects:

            burn = max(1, dragon.stats.hp // 20)

            dragon.current_hp -= burn

            print(
                f"{dragon.name} is hurt by Burn!"
            )

        if "Poison" in dragon.status_effects:

            poison = max(2, dragon.stats.hp // 15)

            dragon.current_hp -= poison

            print(
                f"{dragon.name} suffers Poison damage!"
            )

        if "Freeze" in dragon.status_effects:

            if random.randint(1,100) <= 30:

                dragon.remove_status("Freeze")

                print(
                    f"{dragon.name} thawed out!"
                )

        if dragon.current_hp < 0:

            dragon.current_hp = 0


# ============================================
# Running Away
# ============================================

    def run_attempt(self):

        chance = (
            50
            + self.player.stats.speed
            - self.enemy.stats.speed
        )

        roll = random.randint(1,100)

        if roll <= chance:

            print("You escaped!")

            self.finished = True

            return True

        print("Couldn't escape!")

        return False


# ============================================
# Friendship Bonus
# ============================================

    def friendship_bonus(self, dragon):

        if dragon.friendship >= 100:

            return 1.50

        elif dragon.friendship >= 75:

            return 1.30

        elif dragon.friendship >= 50:

            return 1.15

        return 1.0


# ============================================
# Bond Skill
# ============================================

    def use_bond_skill(self):

        if self.player.friendship < 100:

            print(
                "Bond Skill isn't ready."
            )

            return

        damage = (
            self.player.stats.magic * 3
        )

        self.enemy.current_hp -= damage

        print()

        print(
            self.player.name,
            "used their Bond Skill!"
        )

        print(
            self.enemy.name,
            "took",
            damage,
            "damage!"
        )

        if self.enemy.current_hp < 0:

            self.enemy.current_hp = 0


# ============================================
# Recruit Dragon
# ============================================

    def recruit_enemy(self):

        if self.enemy.corrupted:

            print(
                "Corrupted dragons must be purified first."
            )

            return False

        chance = (
            self.player.friendship
            + self.player.stats.spirit
        )

        roll = random.randint(1,150)

        if roll <= chance:

            print()

            print(
                self.enemy.name,
                "joined your team!"
            )

            return True

        print()

        print(
            self.enemy.name,
            "refused to join."
        )

        return False


# ============================================
# Purify Dragon
# ============================================

    def purify_enemy(self):

        if not self.enemy.corrupted:

            print(
                "This dragon isn't corrupted."
            )

            return False

        chance = (
            self.player.stats.spirit
            + self.player.friendship
        )

        roll = random.randint(1,150)

        if roll <= chance:

            self.enemy.corrupted = False

            print()

            print(
                self.enemy.name,
                "has been purified!"
            )

            return True

        print()

        print(
            "Purification failed!"
        )

        return False
# ============================================
# Move Database
# ============================================

MOVES = {

    "Comet Dash": {
        "power": 40,
        "type": "Star",
        "category": "Physical",
        "accuracy": 95
    },

    "Starlight Aegis": {
        "power": 0,
        "type": "Star",
        "category": "Support",
        "effect": "Shield"
    },

    "Fire Breath": {
        "power": 45,
        "type": "Fire",
        "category": "Magic",
        "accuracy": 90,
        "effect": "Burn"
    },

    "Leaf Slash": {
        "power": 35,
        "type": "Nature",
        "category": "Physical",
        "accuracy": 100
    },

    "Crystal Shield": {
        "power": 0,
        "type": "Crystal",
        "category": "Support",
        "effect": "Defense Up"
    },

    "Shadow Claw": {
        "power": 40,
        "type": "Shadow",
        "category": "Physical",
        "accuracy": 95
    }

}


# ============================================
# Show Moves
# ============================================

    def show_moves(self, dragon):

        print()

        print("Moves")

        print("-----")

        for i, move in enumerate(dragon.moves):

            print(f"{i+1}. {move}")

        print()


# ============================================
# Use Move
# ============================================

    def use_move(self, attacker, defender, move_name):

        if move_name not in MOVES:

            print("Unknown Move")

            return

        move = MOVES[move_name]

        if move["category"] == "Support":

            self.use_support_move(attacker, move_name)

            return

        accuracy = move.get("accuracy",100)

        if random.randint(1,100) > accuracy:

            print(attacker.name, "missed!")

            return

        if move["category"] == "Physical":

            damage = (
                attacker.stats.attack
                + move["power"]
                - defender.stats.defense
            )

        else:

            damage = (
                attacker.stats.magic
                + move["power"]
                - defender.stats.magic_defense
            )

        damage = max(1, damage)

        if self.critical_hit():

            damage *= 2

            print("Critical Hit!")

        defender.current_hp -= damage

        if defender.current_hp < 0:

            defender.current_hp = 0

        print()

        print(attacker.name, "used", move_name)

        print(defender.name, "took", damage, "damage!")

        if "effect" in move:

            effect = move["effect"]

            if effect == "Burn":

                if "Burn" not in defender.status_effects:

                    defender.apply_status("Burn")

                    print(defender.name, "was burned!")


# ============================================
# Support Moves
# ============================================

    def use_support_move(self, dragon, move):

        if move == "Starlight Aegis":

            dragon.stats.defense += 5

            dragon.stats.magic_defense += 5

            print()

            print(dragon.name)

            print("is protected by starlight!")

        elif move == "Crystal Shield":

            dragon.stats.defense += 8

            print()

            print(dragon.name)

            print("raised its Defense!")


# ============================================
# Smarter Enemy AI
# ============================================

    def enemy_turn(self):

        move = random.choice(

            self.enemy.moves

        )

        self.use_move(

            self.enemy,

            self.player,

            move

        )


# ============================================
# Battle Rewards
# ============================================

    def rewards(self):

        coins = random.randint(15,60)

        print()

        print("Battle Rewards")

        print("----------------")

        print(coins, "Coins")

        if random.randint(1,100) <= 25:

            item = random.choice(

                [

                    "Berry",

                    "Healing Herb",

                    "Crystal Shard",

                    "Dragon Feather"

                ]

            )

            print("Found:", item)5
