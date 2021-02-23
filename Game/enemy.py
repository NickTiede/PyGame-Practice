import pygame as pg
import math
import game

width = 800
height = 600
pg.display.set_mode((width, height))

e_img_scale = 0.3


class Enemy(pg.sprite.Sprite):
    def __init__(self, name, x, y, p_x, p_y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(name).convert_alpha()
        w, h = self.image.get_size()
        enemy_dimensions = (int(w * e_img_scale), int(h * e_img_scale))
        self.image = pg.transform.scale(self.image, enemy_dimensions).convert_alpha()
        self.orig_img = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.rect.center = self.pos
        self.rot = 0
        self.p_x = p_x
        self.p_y = p_y
        self.health = 100

    def update(self):
        self.pos = (self.x, self.y)

        player_x, player_y = self.p_x, self.p_y
        enemy_x, enemy_y = self.pos

        self.move_to_player()

        dir_x, dir_y = player_x - enemy_x, player_y - enemy_y

        self.rot = (180 / math.pi) * math.atan2(-dir_y, dir_x) + 7

        self.image = pg.transform.rotate(self.orig_img, self.rot).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move_to_player(self):
        dist = 1  # distance moved in 1 frame
        if self.y < self.p_y:
            self.y += dist  # move down
        elif self.y > self.p_y:
            self.y -= dist  # move up
        if self.x < self.p_x:
            self.x += dist  # move right
        elif self.x > self.p_x:
            self.x -= dist  # move left

    def set_player_pos(self, x, y):
        self.p_x, self.p_y = x, y
        return
