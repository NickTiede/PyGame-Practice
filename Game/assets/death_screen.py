import pygame as pg
import sys
import os
from pygame.locals import *
from timeit import default_timer as timer

width = 800
height = 600

text_color = (200, 100, 100)
text_font = 'arialblack'
text_size = 60

bg_img = os.getcwd() + '/assets/bg1.png'


# Death Screen
def show(screen):
    clock = pg.time.Clock()

    fade = 200
    fade_reverse = False
    fade_time = 5
    fade_start = timer()

    # Create the background for the menu
    bg_image = pg.image.load(bg_img).convert()
    screen.blit(bg_image, (0, 0))

    # Death Fade
    fade_surface = pg.Surface((width, height), pg.SRCALPHA)
    fade_surface.fill((0, 0, 0, fade))
    screen.blit(fade_surface, (0, 0))

    # Death display
    font = pg.font.SysFont(text_font, text_size)
    death_text = font.render('Dead', False, text_color)
    screen.blit(death_text, (width/2 - 80, height/2 - 50))

    # Display loop
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        if not fade_reverse and fade < 255:
            fade += 1
        else:
            fade -= 1

        if fade == 255 and timer() - fade_start >= fade_time:
            fade_reverse = True

        if fade <= 175:
            return

        screen.blit(bg_image, (0, 0))
        fade_surface.fill((0, 0, 0, fade))
        screen.blit(fade_surface, (0, 0))

        if fade >= 220:
            screen.blit(death_text, (width / 2 - 80, height / 2 - 50))

        pg.display.update()

        clock.tick(60)

    return
