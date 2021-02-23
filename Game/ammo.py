import pygame as pg

width = 800
height = 600
pg.display.set_mode((width, height))

a_img_scale = 1


class Ammo(pg.sprite.Sprite):
    def __init__(self, name, x, y, cal, amount):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(name).convert_alpha()
        w, h = self.image.get_size()
        ammo_dimensions = (int(w * a_img_scale), int(h * a_img_scale))
        self.image = pg.transform.scale(self.image, ammo_dimensions).convert_alpha()
        self.orig_img = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.cal = cal
        self.amount = amount
        self.pos = (self.x, self.y)
        self.rect.center = self.pos
        self.rot = 0
        self.gave_ammo = False

    def update(self):
        return
