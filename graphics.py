"""
graphics.py
Wingbound Alliance

Basic graphical overworld
"""

import pygame
import sys


# -----------------------------
# Setup
# -----------------------------

pygame.init()

WIDTH = 640
HEIGHT = 480

TILE_SIZE = 40

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Wingbound Alliance"
)


clock = pygame.time.Clock()


# -----------------------------
# Colors
# -----------------------------

GRASS = (80, 180, 80)
WALL = (80, 80, 80)
TREE = (30, 120, 40)
PLAYER = (40, 90, 220)
DRAGON = (200, 60, 60)
CITY = (170, 140, 80)


# -----------------------------
# Map
# -----------------------------

game_map = [

    "################",

    "#..............#",

    "#....T.........#",

    "#..............#",

    "#......D.......#",

    "#..............#",

    "#..C...........#",

    "################"

]


# -----------------------------
# Player
# -----------------------------

player_x = 2
player_y = 5


# -----------------------------
# Draw Map
# -----------------------------

def draw_world():

    for y, row in enumerate(game_map):

        for x, tile in enumerate(row):

            rect = pygame.Rect(

                x*TILE_SIZE,

                y*TILE_SIZE,

                TILE_SIZE,

                TILE_SIZE

            )


            if tile == "#":

                pygame.draw.rect(
                    screen,
                    WALL,
                    rect
                )


            else:

                pygame.draw.rect(
                    screen,
                    GRASS,
                    rect
                )


            if tile == "T":

                pygame.draw.rect(
                    screen,
                    TREE,
                    rect.inflate(-10,-10)
                )


            if tile == "D":

                pygame.draw.circle(

                    screen,

                    DRAGON,

                    rect.center,

                    15

                )


            if tile == "C":

                pygame.draw.rect(

                    screen,

                    CITY,

                    rect.inflate(-5,-5)

                )


    # Player

    player_rect = pygame.Rect(

        player_x*TILE_SIZE,

        player_y*TILE_SIZE,

        TILE_SIZE,

        TILE_SIZE

    )


    pygame.draw.circle(

        screen,

        PLAYER,

        player_rect.center,

        15

    )


# -----------------------------
# Movement
# -----------------------------

def can_move(x,y):

    if game_map[y][x] == "#":

        return False

    return True



# -----------------------------
# Main Loop
# -----------------------------

running = True


while running:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            running = False



        if event.type == pygame.KEYDOWN:


            new_x = player_x

            new_y = player_y


            if event.key == pygame.K_w:

                new_y -= 1


            if event.key == pygame.K_s:

                new_y += 1


            if event.key == pygame.K_a:

                new_x -= 1


            if event.key == pygame.K_d:

                new_x += 1



            if can_move(new_x,new_y):

                player_x = new_x

                player_y = new_y



    screen.fill((0,0,0))


    draw_world()


    pygame.display.update()


    clock.tick(60)



pygame.quit()

sys.exit()
