import pygame as pg
import sys
from pygame.locals import *
import display as d

bg_color = [10, 10, 40]
button_color = [100, 100, 100]
button_text_color = (200, 200, 200)
button_font = 'Corbel'
button_text_size = 30

# Button dimensions
b_w = 75
b_h = 45


# Game loop
def open_instr(screen):

    w, h = pg.display.get_surface().get_size()

    # Create the background
    screen.fill(bg_color)
    font = pg.font.SysFont('Corbel', 30)
    text = font.render('Instructions', False, button_text_color)
    screen.blit(text, (100, 100))

    back_button = pg.Rect((w * 3/4) - b_w/2, (h * 3/4) - b_h/2, b_w, b_h)
    pg.draw.rect(screen, button_color, back_button)
    font = pg.font.SysFont(button_font, button_text_size)
    back_text = font.render('Back', False, button_text_color)
    screen.blit(back_text, (back_button.left + 10, back_button.top + 10))

    # Main menu loop
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if back_button.collidepoint(mouse_pos):
                    print('Back button was pressed')
                    return 'menu'

        pg.display.update()

    return 0
