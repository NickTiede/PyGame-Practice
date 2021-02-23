import pygame as pg
import sys
import os
from pygame.locals import *
from timeit import default_timer as timer
from ammo import Ammo
from player import Player
from enemy import Enemy
import random

width = 800
height = 600

text_color = (200, 200, 200)
text_font = 'arialblack'
text_size = 35

player_img = os.getcwd() + '/assets/survivor-idle_rifle_0.png'
enemy_img = os.getcwd() + '/assets/skeleton-attack_0.png'
ammo_img = os.getcwd() + '/assets/Ammo.png'
bg_img = os.getcwd() + '/assets/bg1.png'
ui_bg_img = os.getcwd() + '/assets/player_ui_bg.png'

damage_dist = 20
knife_dist = 40
ammo_dist = 25
ammo_amount = 10

# Times
flash_time = 0.05
hit_time = 0.07
reload_time = 2
knife_time = 0.5


# Game loop
def play_game(screen):

    clock = pg.time.Clock()
    pg.mouse.set_cursor(*pg.cursors.broken_x)

    bg_image = pg.image.load(bg_img).convert()
    screen.blit(bg_image, (0, 0))

    # Health Fade
    health_surface = pg.Surface((width, height - 50), pg.SRCALPHA)
    health_surface.fill((0, 0, 0, 0))
    screen.blit(health_surface, (0, 0))

    # List of all sprites
    all_sprites_list = pg.sprite.Group()

    # Temporary creates ammo
    a = Ammo(ammo_img, -50, -50, 'rifle', ammo_amount)
    all_sprites_list.add(a)

    # Timer starts
    flash_start = timer()
    hit_start = timer()
    reload_start = 0
    knife_start = 0

    # Creates player character
    pc = Player(player_img, width/2, height/2)
    all_sprites_list.add(pc)
    p_health = pc.health

    # Creates enemy
    e = Enemy(enemy_img, -50, -50, pc.x, pc.y)
    all_sprites_list.add(e)

    # Player UI
    ui_bg_image = pg.image.load(ui_bg_img).convert_alpha()
    screen.blit(ui_bg_image, (0, height - 50))

    # Health display
    font = pg.font.SysFont(text_font, text_size)
    health_text = font.render('Health: ' + str(pc.health), False, text_color)
    screen.blit(health_text, (10, height - 50))

    # Ammo display
    font = pg.font.SysFont(text_font, text_size)
    ammo_text = font.render('Ammo: ' + str(pc.clip) + ' / ' + str(pc.ammo), False, text_color)
    screen.blit(ammo_text, (255, height - 50))

    # Health display
    font = pg.font.SysFont(text_font, text_size)
    points_text = font.render('Points: ' + str(pc.points), False, text_color)
    screen.blit(points_text, (555, height - 50))

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            # Reload
            if event.type == KEYDOWN and pg.key.get_pressed()[ord('r')]:
                if timer() - reload_start >= reload_time:
                    reload_start = timer()
                    pc.image_num = 2
                    pc.update()
                    ammo_loaded = pc.clip_size - pc.clip
                    if pc.ammo >= ammo_loaded:
                        pc.ammo -= ammo_loaded
                        pc.clip += ammo_loaded
                    else:
                        pc.clip += pc.ammo
                        pc.ammo = 0
            # Knife
            if event.type == KEYDOWN and pg.key.get_pressed()[pg.K_SPACE]:
                knife_start = timer()
                pc.image_num = 3
                pc.update()

                if abs(e.x - pc.x) <= knife_dist and abs(e.y - pc.y) <= knife_dist:
                    e.health -= 50
                    hit_start = timer()
                    e.image_num = 1
                    e.update()

            # Shoot
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()

                if timer() - reload_start >= reload_time:
                    if pc.clip > 0:
                        # Use ammo in clip
                        pc.clip -= 1

                        # Changes player image to firing
                        flash_start = timer()
                        pc.image_num = 1
                        pc.update()

                        # Deal damage when clicking on enemy
                        if e.rect.collidepoint(pos):
                            e.health -= 20
                            hit_start = timer()
                            e.image_num = 1
                            e.update()

        # Normal player image if no muzzle flash, reload, or knife
        flash_calc = timer() - flash_start >= flash_time
        reload_calc = timer() - reload_start >= reload_time
        knife_calc = timer() - knife_start >= knife_time
        if flash_calc and reload_calc and knife_calc:
            pc.image_num = 0

        # Enemy hit image
        if timer() - hit_start >= hit_time:
            e.image_num = 0

        # Enemy dies
        if e.health <= 0:
            pc.points += 1

            all_sprites_list.remove(a)
            a = Ammo(ammo_img, e.x, e.y, 'rifle', ammo_amount)
            all_sprites_list.add(a)

            all_sprites_list.remove(e)
            rand_x, rand_y = get_rand_enemy_pos()
            e = Enemy(enemy_img, rand_x, rand_y, pc.x, pc.y)
            all_sprites_list.add(e)

        # Updates sprite information
        e.set_player_pos(pc.x, pc.y)
        all_sprites_list.update()

        # Enemy attacking player
        if abs(e.x - pc.x) <= damage_dist and abs(e.y - pc.y) <= damage_dist:
            pc.health -= 1

        # Picking up ammo
        if abs(a.x - pc.x) <= ammo_dist and abs(a.y - pc.y) <= ammo_dist and not a.gave_ammo:
            pc.ammo += a.amount
            a.gave_ammo = True
            all_sprites_list.remove(a)
            all_sprites_list.update()

        # Player status text updates
        health_text = font.render('Health: ' + str(pc.health), False, text_color)
        screen.blit(health_text, (10, height - 50))

        # Ammo text updates
        ammo_text = font.render('Ammo: ' + str(pc.clip) + ' / ' + str(pc.ammo), False, text_color)

        if timer() - reload_start < reload_time:
            ammo_text = font.render('Ammo: RLD', False, text_color)
        screen.blit(ammo_text, (255, height - 50))

        # Points text updates
        points_text = font.render('Points: ' + str(pc.points), False, text_color)
        screen.blit(points_text, (555, height - 50))

        # On death
        if pc.health <= 0:
            return

        # Redraws screen and background
        pg.display.update()

        screen.blit(bg_image, (0, 0))

        # Redraws sprites
        all_sprites_list.draw(screen)

        screen.blit(ui_bg_image, (0, height - 50))

        # Health fade
        health_surface.fill((0, 0, 0, 2 * (p_health - pc.health)))
        screen.blit(health_surface, (0, 0))

        clock.tick(60)


def get_rand_enemy_pos():
    off_dist = 50
    side = random.randint(1, 5)

    x_loc = random.randrange(width)
    y_loc = random.randrange(height)

    if side == 1:
        return random.randint(0 - off_dist, width + off_dist), 0 - off_dist
    elif side == 2:
        return width + off_dist, random.randint(0 - off_dist, height + off_dist)
    elif side == 3:
        return random.randint(0 - off_dist, width + off_dist), height + off_dist
    elif side == 4:
        return 0 - off_dist, random.randint(0 - off_dist, height + off_dist)

    return 0, 0
