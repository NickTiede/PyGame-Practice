import pygame as pg
import math
import os
from display import rot_center

width = 800
height = 600
pg.display.set_mode((width, height))

p_img_scale = 0.3
player_firing_img = os.getcwd() + '/assets/pc_firing.png'
player_reload_img = os.getcwd() + '/assets/player_reload.png'
player_knife_img = os.getcwd() + '/assets/player_knife.png'


class Player(pg.sprite.Sprite):
    def __init__(self, name, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(name).convert_alpha()
        w, h = self.image.get_size()
        player_dimensions = (int(w * p_img_scale), int(h * p_img_scale))
        self.image = pg.transform.scale(self.image, player_dimensions).convert_alpha()
        self.orig_img = self.image
        self.rect = self.image.get_rect()
        self.fire_img = pg.image.load(player_firing_img).convert_alpha()
        self.fire_img = pg.transform.scale(self.fire_img, player_dimensions).convert_alpha()
        self.reload_img = pg.image.load(player_reload_img).convert_alpha()
        self.reload_img = pg.transform.scale(self.reload_img, player_dimensions).convert_alpha()
        self.knife_img = pg.image.load(player_knife_img).convert_alpha()
        self.knife_img = pg.transform.scale(self.knife_img, player_dimensions).convert_alpha()
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.rect.center = self.pos
        self.rot = 0
        self.health = 100
        self.ammo = 10
        self.clip = 10
        self.clip_size = 10
        self.image_num = 0
        self.points = 0

    def update(self):
        self.handle_keys()
        self.pos = (self.x, self.y)

        mouse_x, mouse_y = pg.mouse.get_pos()
        player_x, player_y = self.pos

        dir_x, dir_y = mouse_x - player_x, mouse_y - player_y

        self.rot = (180 / math.pi) * math.atan2(-dir_y, dir_x) + 7

        if self.image_num == 0:
            current_img = self.orig_img
            self.image = pg.transform.rotate(current_img, self.rot).convert_alpha()
            self.rect = self.image.get_rect()
        elif self.image_num == 1:
            current_img = self.fire_img
            self.image = pg.transform.rotate(current_img, self.rot).convert_alpha()
            self.rect = self.image.get_rect()
        elif self.image_num == 2:
            current_img = self.reload_img
            self.image = pg.transform.rotate(current_img, self.rot).convert_alpha()
            self.rect = self.image.get_rect()
        elif self.image_num == 3:
            current_img = self.knife_img
            self.image = pg.transform.rotate(current_img, self.rot).convert_alpha()
            self.rect = self.image.get_rect()

        self.rect.center = self.pos

    def handle_keys(self):
        key = pg.key.get_pressed()
        dist = 3  # distance moved in 1 frame
        from_wall = 42
        if (key[pg.K_DOWN] or key[ord('s')]) and self.y <= height - from_wall - 50:  # down key
            self.y += dist  # move down
        elif (key[pg.K_UP] or key[ord('w')]) and self.y >= from_wall:  # up key
            self.y -= dist  # move up
        if (key[pg.K_RIGHT] or key[ord('d')]) and self.x <= width - from_wall:  # right key
            self.x += dist  # move right
        elif (key[pg.K_LEFT] or key[ord('a')]) and self.x >= from_wall:  # left key
            self.x -= dist  # move left
