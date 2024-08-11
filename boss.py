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

class boss():
    def __init__(self):
        super(boss, self).__init__()
        # self.surf = pygame.image.load("pypygame/source/png/player.png").convert()
        # self.surf.set_colorkey((255,255,255), RLEACCEL)
        # self.rect = self.surf.get_rect(center=(width/2, height/2))