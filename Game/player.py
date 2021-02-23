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
        self.image = pg.image.load(name).convert()
        w, h = self.image.get_size()
        player_dimensions = (int(w * p_img_scale), int(h * p_img_scale))
        self.image = pg.transform.scale(self.image, player_dimensions)
        self.orig_img = self.image
        self.rect = self.image.get_rect()
        self.pos = (x, y)
        self.rect.center = self.pos
        self.rot = 0

    def update(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        player_x, player_y = self.pos

        dir_x, dir_y = mouse_x - player_x, mouse_y - player_y

        self.rot = (180 / math.pi) * math.atan2(-dir_y, dir_x) + 7

        self.image = pg.transform.rotate(self.orig_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


