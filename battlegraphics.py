import pygame
import random


# ============================================
# BATTLE GRAPHICS
# ============================================

def start_battle_graphics(player_dragon, enemy_dragon):

    pygame.init()

    WIDTH = 900
    HEIGHT = 600

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )

    pygame.display.set_caption(
        "Wingbound Alliance Battle"
    )


    clock = pygame.time.Clock()


    font = pygame.font.SysFont(
        None,
        40
    )

    small_font = pygame.font.SysFont(
        None,
        28
    )


    # Colors

    SKY = (130,200,255)
    GRASS = (80,180,80)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (50,200,50)
    RED = (220,50,50)
    BUTTON = (180,180,220)



    # Buttons

    moves = player_dragon.moves


    buttons = []

    for i, move in enumerate(moves):

        button = pygame.Rect(
            50 + i*210,
            500,
            180,
            60
        )

        buttons.append(
            (button, move)
        )



    def draw_hp(x,y,current,max_hp,name):

        pygame.draw.rect(
            screen,
            RED,
            (x,y,250,25)
        )

        amount = int(
            250*(current/max_hp)
        )

        pygame.draw.rect(
            screen,
            GREEN,
            (x,y,amount,25)
        )


        text = small_font.render(
            f"{name}: {current}/{max_hp}",
            True,
            BLACK
        )

        screen.blit(
            text,
            (x,y-35)
        )



    def draw_dragon(dragon,x,y):

        sprite = font.render(
            dragon.sprite,
            True,
            BLACK
        )

        screen.blit(
            sprite,
            (x,y)
        )


    def attack(move):

        damage = (

            player_dragon.attack
            + random.randint(5,20)

        )

        enemy_dragon.hp -= damage


        if enemy_dragon.hp < 0:

            enemy_dragon.hp = 0


        print(
            player_dragon.name,
            "used",
            move,
            "!"
        )


        print(
            enemy_dragon.name,
            "lost",
            damage,
            "HP"
        )


    running = True


    while running:


        for event in pygame.event.get():


            if event.type == pygame.QUIT:

                running = False



            if event.type == pygame.MOUSEBUTTONDOWN:


                for rect,move in buttons:

                    if rect.collidepoint(
                        event.pos
                    ):

                        attack(move)


        screen.fill(SKY)


        # Ground

        pygame.draw.rect(
            screen,
            GRASS,
            (0,300,900,300)
        )


        # Dragons

        draw_dragon(
            player_dragon,
            150,
            250
        )


        draw_dragon(
            enemy_dragon,
            650,
            250
        )


        # HP

        draw_hp(
            50,
            70,
            player_dragon.hp,
            player_dragon.max_hp,
            player_dragon.name
        )


        draw_hp(
            600,
            70,
            enemy_dragon.hp,
            enemy_dragon.max_hp,
            enemy_dragon.name
        )



        # Buttons

        for rect,move in buttons:

            pygame.draw.rect(
                screen,
                BUTTON,
                rect
            )

            text = small_font.render(
                move,
                True,
                BLACK
            )

            screen.blit(
                text,
                (
                    rect.x+10,
                    rect.y+15
                )
            )


        # Victory text

        if enemy_dragon.hp <= 0:

            victory = font.render(
                "Dragon Recruited!",
                True,
                BLACK
            )

            screen.blit(
                victory,
                (300,150)
            )



        pygame.display.update()

        clock.tick(60)



    pygame.quit()
