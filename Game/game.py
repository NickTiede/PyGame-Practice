import pygame as pg
import sys
import os
from pygame.locals import *

from ammo import Ammo
from player import Player
from enemy import Enemy
from random import randrange

width = 800
height = 600

text_color = (255, 75, 75)
text_font = 'arialblack'
text_size = 40

player_img = os.getcwd() + '/assets/survivor-idle_rifle_0.png'
enemy_img = os.getcwd() + '/assets/skeleton-attack_0.png'
ammo_img = os.getcwd() + '/assets/Ammo.png'
bg_img = os.getcwd() + '/assets/bg1.png'

damage_dist = 20
ammo_dist = 20


# Game loop
def play_game(screen):

    clock = pg.time.Clock()
    pg.mouse.set_cursor(*pg.cursors.broken_x)

    bg_image = pg.image.load(bg_img).convert()
    screen.blit(bg_image, (0, 0))

    # List of all sprites
    all_sprites_list = pg.sprite.Group()

    # Temporary creates ammo
    a = Ammo(ammo_img, 100, 100, 'rifle', 2)
    all_sprites_list.add(a)

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

    # Ammo display
    font = pg.font.SysFont(text_font, text_size)
    ammo_text = font.render('Ammo: ' + str(pc.clip) + ' / ' + str(pc.ammo), False, text_color)
    screen.blit(ammo_text, (width - 350, height - 50))

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN and pg.key.get_pressed()[pg.K_SPACE]:
                ammo_loaded = pc.clip_size - pc.clip
                if pc.ammo >= ammo_loaded:
                    pc.ammo -= ammo_loaded
                    pc.clip += ammo_loaded
                else:
                    pc.clip += pc.ammo
                    pc.ammo = 0

            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()

                if pc.clip > 0:
                    # Use ammo in clip
                    pc.clip -= 1

                    # Deal damage when clicking on enemy
                    if e.rect.collidepoint(pos):
                        e.health -= 20

        # Enemy dies
        if e.health <= 0:
            all_sprites_list.remove(a)
            a = Ammo(ammo_img, e.x, e.y, 'rifle', 2)
            all_sprites_list.add(a)

            all_sprites_list.remove(e)
            e = Enemy(enemy_img, randrange(width), randrange(height), pc.x, pc.y)
            all_sprites_list.add(e)

        # Updates sprite information
        e.set_player_pos(pc.x, pc.y)
        all_sprites_list.update()

        # Enemy attacking player
        if abs(e.x - pc.x) <= damage_dist and abs(e.y - pc.y) <= damage_dist:
            pc.health -= 1

        # Picking up ammo
        if abs(a.x - pc.x) <= ammo_dist and abs(a.y - pc.y) <= ammo_dist:
            pc.ammo += a.amount
            all_sprites_list.remove(a)
            all_sprites_list.update()

        # Player status text updates
        health_text = font.render('Health: ' + str(pc.health), False, text_color)
        screen.blit(health_text, (10, height - 50))
        ammo_text = font.render('Ammo: ' + str(pc.clip) + ' / ' + str(pc.ammo), False, text_color)
        screen.blit(ammo_text, (width - 350, height - 50))

        if pc.health <= 0:
            return

        # Redraws screen and background
        pg.display.update()

        screen.blit(bg_image, (0, 0))

        # Redraws sprites
        all_sprites_list.draw(screen)

        clock.tick(60)



