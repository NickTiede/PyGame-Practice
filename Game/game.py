import pygame as pg
import sys
import os
from pygame.locals import *
from player import Player
from enemy import Enemy
from random import randrange

width = 800
height = 600

text_color = (255, 75, 75)
text_font = 'Corbel'
text_size = 40

player_img = os.getcwd() + '/assets/survivor-idle_rifle_0.png'
enemy_img = os.getcwd() + '/assets/skeleton-attack_0.png'

bg_img = os.getcwd() + '/assets/bg1.png'

damage_dist = 20


# Game loop
def play_game(screen):

    clock = pg.time.Clock()
    pg.mouse.set_cursor(*pg.cursors.broken_x)

    bg_image = pg.image.load(bg_img).convert()
    screen.blit(bg_image, (0, 0))

    # List of all sprites
    all_sprites_list = pg.sprite.Group()

    # Creates player character
    pc = Player(player_img, width/2, height/2)
    all_sprites_list.add(pc)

    # Creates enemy
    e = Enemy(enemy_img, 50, 50, pc.x, pc.y)
    all_sprites_list.add(e)

    # Health display
    font = pg.font.SysFont(text_font, text_size)
    health_text = font.render('Health: ' + str(pc.health), False, text_color)
    screen.blit(health_text, (10, height - 50))

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()

                # Deal damage when clicking on enemy
                if e.rect.collidepoint(pos):
                    e.health -= 20

        if e.health <= 0:
            all_sprites_list.remove(e)
            e = Enemy(enemy_img, randrange(width), randrange(height), pc.x, pc.y)
            all_sprites_list.add(e)

        # Updates sprite information
        e.set_player_pos(pc.x, pc.y)
        all_sprites_list.update()

        # Enemy attacking player
        if abs(e.x - pc.x) <= damage_dist and abs(e.y - pc.y) <= damage_dist:
            pc.health -= 1

        health_text = font.render('Health: ' + str(pc.health), False, text_color)
        screen.blit(health_text, (10, height - 50))

        if pc.health <= 0:
            return

        # Redraws screen and background
        pg.display.update()

        screen.blit(bg_image, (0, 0))

        # Redraws sprites
        all_sprites_list.draw(screen)

        clock.tick(60)



