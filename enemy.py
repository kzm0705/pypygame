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
    QUIT,)



width = 450
height = 600


class Enemy():
    def __init__(self):
        self.surf = pygame.image.load("pypygame/source/png/enemy.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(100,100))



