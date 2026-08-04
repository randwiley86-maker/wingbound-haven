# ============================================
# SAVE SYSTEM
# ============================================

SAVE_FILE = "wingbound_save.json"



def dragon_to_dict(dragon):

    return {

        "name": dragon.name,

        "species": dragon.species,

        "sprite": dragon.sprite,

        "level": dragon.level,

        "hp": dragon.hp,

        "max_hp": dragon.max_hp,

        "attack": dragon.attack,

        "defense": dragon.defense,

        "speed": dragon.speed,

        "friendship": dragon.friendship,

        "moves": dragon.moves

    }



def save_game(player_name, coins, dragons):

    data = {

        "player_name": player_name,

        "coins": coins,

        "dragons": []

    }


    for dragon in dragons:

        data["dragons"].append(
            dragon_to_dict(dragon)
        )


    with open(
        SAVE_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


    print("Game saved!")



def load_game():

    if not os.path.exists(SAVE_FILE):

        print("No save file found.")

        return None



    with open(
        SAVE_FILE,
        "r"
    ) as file:

        data = json.load(file)


    print("Game loaded!")

    return data
