import pygame
from pygame.locals import *
import player
import enemy
import boss
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

import math

width = 450
height = 600


class Enemy():
    def __init__(self):
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

    def enemy_update(self):
        # if self.count >= 3.14 / 180:
        #     self.count = 0
        self.count += self.a / 3.14
        self.rad = self.count

        y = int(self.radius * math.sin(self.rad)) + self.y_center
        x = int(self.radius * math.cos(self.rad)) + self.x_center

        self.rect.x = x
        self.rect.y = y
