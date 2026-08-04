# ============================================
# TEAM SYSTEM
# ============================================


class DragonTeam:

    def __init__(self):

        # Dragons currently ready for battle

        self.team = []


        # Extra dragons stored away

        self.storage = []



    # --------------------------
    # Add Dragon
    # --------------------------

    def add_dragon(self, dragon):

        if len(self.team) < 6:

            self.team.append(dragon)

            print(
                dragon.name,
                "joined your team!"
            )

        else:

            self.storage.append(dragon)

            print(
                dragon.name,
                "was sent to storage."
            )



    # --------------------------
    # Remove Dragon
    # --------------------------

    def remove_dragon(self, dragon):

        if dragon in self.team:

            self.team.remove(dragon)

            print(
                dragon.name,
                "left the team."
            )


        elif dragon in self.storage:

            self.storage.remove(dragon)



    # --------------------------
    # Switch Active Dragon
    # --------------------------

    def switch_dragon(self, number):

        if number < 1 or number > len(self.team):

            print(
                "Invalid dragon."
            )

            return None


        active = self.team[number-1]


        print(
            "Active dragon:",
            active.name
        )


        return active



    # --------------------------
    # Show Team
    # --------------------------

    def show_team(self):

        print()

        print("================")

        print("YOUR DRAGONS")

        print("================")


        if len(self.team) == 0:

            print(
                "No dragons yet!"
            )

            return


        for i, dragon in enumerate(self.team):

            print(

                str(i+1)
                + ".",

                dragon.name,

                "-",

                dragon.species,

                "Lv.",
                dragon.level

            )



    # --------------------------
    # Show Storage
    # --------------------------

    def show_storage(self):

        print()

        print("DRAGON STORAGE")


        for dragon in self.storage:

            print(

                dragon.name,

                dragon.species

            )
