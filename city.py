# ============================================
# CITY SYSTEM
# ============================================


class City:


    def __init__(self, name):

        self.name = name


        self.buildings = [

            "Dragon Center",

            "Hatchery",

            "Breeding Lab",

            "Shop"

        ]


        self.npcs = [

            "Professor Nova",

            "Breeder Mira",

            "Shopkeeper Finn",

            "Trainer Kai"

        ]



    # --------------------------
    # Show City
    # --------------------------

    def show_city(self):

        print()

        print("================")

        print(self.name)

        print("================")


        print()

        print("Buildings:")


        for building in self.buildings:

            print(
                "-",
                building
            )


        print()

        print("People:")


        for npc in self.npcs:

            print(
                "-",
                npc
            )



    # --------------------------
    # Dragon Center
    # --------------------------

    def dragon_center(self, team):

        print()

        print(
            "Welcome to the Dragon Center!"
        )


        for dragon in team.team:

            dragon.hp = dragon.max_hp


        print(
            "All dragons healed!"
        )



    # --------------------------
    # Shop
    # --------------------------

    def shop(self, inventory):

        print()

        print(
            "Shop"
        )


        print(
            "1. Dragon Berry - 10 coins"
        )

        print(
            "2. Healing Herb - 20 coins"
        )



    # --------------------------
    # Hatchery
    # --------------------------

    def hatchery(self, inventory):

        print()

        print(
            "The Hatchery checks your eggs..."
        )


        print(

            "Eggs:",

            len(inventory.eggs)

        )



    # --------------------------
    # Breeding Lab
    # --------------------------

    def breeding_lab(self):

        print()

        print(
            "Welcome to the Breeding Lab!"
        )

        print(
            "Choose two dragons to create an egg."
        )
