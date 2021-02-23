import pygame as pg
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
b_h = 50


# Game loop
def open_menu(screen):

    w, h = pg.display.get_surface().get_size()

    # Create the background for the menu
    screen.fill(bg_color)

    start_button = pg.Rect(w/2 - b_w/2, h/2 - b_h/2 + 120, b_w, b_h)
    pg.draw.rect(screen, button_color, start_button)
    font = pg.font.SysFont(button_font, button_text_size)
    start_text = font.render('Start Game', False, button_text_color)
    screen.blit(start_text, (start_button.left + 10, start_button.top + 10))

    instr_button = pg.Rect(w/2 - b_w/2, h/2 - b_h/2 + 180, b_w, b_h)
    pg.draw.rect(screen, button_color, instr_button)
    font = pg.font.SysFont(button_font, button_text_size)
    instr_text = font.render('Instructions', False, button_text_color)
    screen.blit(instr_text, (instr_button.left + 10, instr_button.top + 10))

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