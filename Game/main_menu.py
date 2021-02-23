import pygame as pg
import os
import sys
from pygame.locals import *
import display as d

bg_color = [0, 0, 0]
button_color = [100, 100, 100]
button_text_color = (200, 200, 200)
button_font = 'Corbel'
button_text_size = 40

# Button dimensions
b_w = 200
b_h = 43

start_button_img = os.getcwd() + '/assets/start_button.png'
controls_button_img = os.getcwd() + '/assets/controls_button.png'


# Game loop
def open_menu(screen):

    w, h = pg.display.get_surface().get_size()

    # Create the background for the menu
    bg_img = os.getcwd() + '/assets/bg1.png'
    bg_image = pg.image.load(bg_img).convert()
    screen.blit(bg_image, (0, 0))

    start_image = pg.image.load(start_button_img).convert_alpha()
    start_button = pg.Rect((w/2 - b_w/2, h/2 - b_h/2 + 50), (b_w, b_h))
    screen.blit(start_image, start_button)

    controls_image = pg.image.load(controls_button_img).convert_alpha()
    instr_button = pg.Rect((w / 2 - b_w / 2, h / 2 - b_h / 2 + 100), (b_w, b_h))
    screen.blit(controls_image, instr_button)

    # Main menu loop
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if start_button.collidepoint(mouse_pos):
                    print('Start button was pressed')
                    return 'game'

                if instr_button.collidepoint(mouse_pos):
                    print('Instructions button was pressed')
                    return 'instructions'

        pg.display.update()

    return 0
