import pygame as pg
import sys
import os
from pygame.locals import *
from player import Player
import display

width = 800
height = 600

player_img = os.getcwd() + '/assets/survivor-idle_rifle_0.png'


# Game loop
def play_game(screen):
    clock = pg.time.Clock()

    # Temp just to show you're in game loop
    screen.fill([0, 0, 0])
    font = pg.font.SysFont('Comic Sans MS', 30)
    text = font.render('Game loop', False, (200, 200, 200))
    screen.blit(text, (100, 100))

    # List of all sprites
    all_sprites_list = pg.sprite.Group()

    # Creates player character
    pc = Player(player_img, width/2, height/2)
    all_sprites_list.add(pc)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        # Updates sprite information
        all_sprites_list.update()

        # Redraws screen and background
        pg.display.update()

        # Redraws sprites
        all_sprites_list.draw(screen)

        clock.tick(60)



