import pygame
from pygame.locals import *
import math

boss_HP = 0

class boss():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("pypygame/source/png/enemy.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(100,100))
        self.radius = 80
        self.y_center = 50
        self.x_center = 80
        self.count = 0
        self.a = 3.14/360
        self.deg = 0
        self.rad = 0

        boss_HP = 100



    def boss_update(self):
        #ボスを楕円形に移動させる
        # if self.count >= 3.14 / 180:
        #      self.count = 0
        self.count += self.a / 3.14
        self.rad = self.count * 10

        y = int(self.radius * math.sin(self.rad)) + self.y_center + 10
        x = int(self.radius * math.cos(self.rad)) + self.x_center + 10

        self.rect.x = x
        self.rect.y = y













