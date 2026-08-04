# ============================================
# BREEDING AND EGGS
# ============================================

import random


class Egg:

    def __init__(self, parent1, parent2):

        self.parent1 = parent1
        self.parent2 = parent2

        self.steps = 0

        self.ready = False


    def hatch_progress(self, amount):

        self.steps += amount

        if self.steps >= 100:

            self.ready = True



def create_egg(dragon1, dragon2):

    print(
        dragon1.name,
        "and",
        dragon2.name,
        "created an egg!"
    )

    return Egg(
        dragon1,
        dragon2
    )



def hatch_egg(egg):

    if not egg.ready:

        print(
            "The egg is not ready yet!"
        )

        return None



    # Rare breeding species

    breeding_species = {


        ("Star Dragon","Fire Dragon"):
            "Solar Dragon",


        ("Water Dragon","Storm Dragon"):
            "Tempest Dragon",


        ("Crystal Dragon","Shadow Dragon"):
            "Night Crystal Dragon"

    }


    parents = (

        egg.parent1.species,

        egg.parent2.species

    )


    if parents in breeding_species:

        species = breeding_species[parents]


    else:

        species = random.choice(

            [

                egg.parent1.species,

                egg.parent2.species

            ]

        )


    baby = Dragon(

        "Baby " + species,

        species,

        "🥚",

        50,

        10,

        10,

        10

    )


    baby.friendship = 20


    print()

    print(
        "The egg hatched!"
    )

    print(
        baby.name,
        "was born!"
    )


    return baby
