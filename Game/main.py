import pygame as pg
import sys
from pygame.locals import *
import display
import game
import main_menu
import instr_menu

# Initializes required modules
pg.init()

# Creates game window
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Game')

# Screen currently displayed
# 'menu', 'instructions', 'game'
screen_choice = 'menu'

# Menu loop
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()

    # Main menu loop
    if screen_choice == 'menu':
        screen_choice = main_menu.open_menu(screen)

    # Instructions menu loop
    if screen_choice == 'instructions':
        screen_choice = instr_menu.open_instr(screen)

    # Game loop
    if screen_choice == 'game':
        game.play_game(screen)
