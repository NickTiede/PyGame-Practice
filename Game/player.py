import pygame as pg
import math
from display import rot_center

width = 800
height = 600
pg.display.set_mode((width, height))

p_img_scale = 0.3


class Player(pg.sprite.Sprite):
    def __init__(self, name, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(name).convert_alpha()
        w, h = self.image.get_size()
        player_dimensions = (int(w * p_img_scale), int(h * p_img_scale))
        self.image = pg.transform.scale(self.image, player_dimensions).convert_alpha()
        self.orig_img = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.rect.center = self.pos
        self.rot = 0
        self.health = 100
        self.ammo = 20
        self.clip = 0
        self.clip_size = 10

    def update(self):
        self.handle_keys()
        self.pos = (self.x, self.y)

        mouse_x, mouse_y = pg.mouse.get_pos()
        player_x, player_y = self.pos

        dir_x, dir_y = mouse_x - player_x, mouse_y - player_y

        self.rot = (180 / math.pi) * math.atan2(-dir_y, dir_x) + 7

        self.image = pg.transform.rotate(self.orig_img, self.rot).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def handle_keys(self):
        key = pg.key.get_pressed()
        dist = 3  # distance moved in 1 frame
        from_wall = 42
        if (key[pg.K_DOWN] or key[ord('s')]) and self.y <= height - from_wall:  # down key
            self.y += dist  # move down
        elif (key[pg.K_UP] or key[ord('w')]) and self.y >= from_wall:  # up key
            self.y -= dist  # move up
        if (key[pg.K_RIGHT] or key[ord('d')]) and self.x <= width - from_wall:  # right key
            self.x += dist  # move right
        elif (key[pg.K_LEFT] or key[ord('a')]) and self.x >= from_wall:  # left key
            self.x -= dist  # move left
