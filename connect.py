# ============================================
# main.py
# Wingbound Alliance Connector
# ============================================


from BaseDragons import Dragon

from bag import Inventory

from battle import Battle

from BattleGraphics import start_battle_graphics

from city import City

from eggs import Egg, create_egg

from graphics import start_world

from save import save_game, load_game

from world import World



# ============================================
# Create Player Data
# ============================================


class Player:

    def __init__(self, name):

        self.name = name

        self.coins = 100

        self.dragons = []

        self.inventory = Inventory()



    def add_dragon(self, dragon):

        self.dragons.append(dragon)

        print(
            dragon.name,
            "joined your team!"
        )



# ============================================
# Start Game
# ============================================


def start_game():

    print(
        "Welcome to Wingbound Alliance!"
    )


    player = Player(
        "Dragon Trainer"
    )


    # Create starting dragon

    alice = Dragon(

        "Alice",

        "Star Dragon",

        "🐉",

        100,

        20,

        15,

        10

    )


    alice.moves = [

        "Comet Dash"

    ]


    player.add_dragon(alice)



    # Create world

    world = World()


    city = City(
        "Dragon's Rest"
    )



    while True:


        print()

        print("================")

        print("MAIN MENU")

        print("================")

        print("1. Explore")

        print("2. Visit City")

        print("3. Team")

        print("4. Inventory")

        print("5. Save")

        print("6. Quit")


        choice = input("> ")



        if choice == "1":

            start_world(player)



        elif choice == "2":

            city.show_city()



        elif choice == "3":

            for dragon in player.dragons:

                print(
                    dragon.name,
                    dragon.species
                )



        elif choice == "4":

            player.inventory.show_inventory()



        elif choice == "5":

            save_game(player)



        elif choice == "6":

            print(
                "Goodbye!"
            )

            break





if __name__ == "__main__":

    start_game()
