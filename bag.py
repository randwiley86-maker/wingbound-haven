# ============================================
# INVENTORY SYSTEM
# ============================================


class Inventory:

    def __init__(self):

        self.items = {

            "Dragon Berry": 5,

            "Healing Herb": 3,

            "Dragon Crystal": 0

        }


        self.eggs = []


        self.coins = 100



    # --------------------------
    # Add Item
    # --------------------------

    def add_item(self, item, amount=1):

        if item not in self.items:

            self.items[item] = 0


        self.items[item] += amount


        print(
            "Got",
            amount,
            item
        )



    # --------------------------
    # Remove Item
    # --------------------------

    def remove_item(self, item, amount=1):

        if item not in self.items:

            print(
                "You don't have that item!"
            )

            return False


        if self.items[item] < amount:

            print(
                "Not enough!"
            )

            return False


        self.items[item] -= amount


        return True



    # --------------------------
    # Check Item
    # --------------------------

    def has_item(self, item):

        return (

            item in self.items

            and self.items[item] > 0

        )



    # --------------------------
    # Add Egg
    # --------------------------

    def add_egg(self, egg):

        self.eggs.append(
            egg
        )


        print(
            "You received an egg!"
        )



    # --------------------------
    # Spend Coins
    # --------------------------

    def spend_coins(self, amount):

        if self.coins >= amount:

            self.coins -= amount

            return True


        return False



    # --------------------------
    # Gain Coins
    # --------------------------

    def gain_coins(self, amount):

        self.coins += amount



    # --------------------------
    # Show Inventory
    # --------------------------

    def show_inventory(self):

        print()

        print("================")

        print("INVENTORY")

        print("================")


        print(
            "Coins:",
            self.coins
        )


        print()


        for item, amount in self.items.items():

            print(
                item,
                "x",
                amount
            )


        print()


        print(
            "Eggs:",
            len(self.eggs)
        )
