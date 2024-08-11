import pygame
from pygame.sprite import Sprite
from pygame.locals import *
import player
import enemy
import boss

class Bullet(Sprite):
    def __init__(self,):
        super().__init__()
        self.rect = pygame.Rect(230,550,5,50)
        self.y = float(self.rect.y)

    def draw_bullet(self,screen):
        pygame.draw.rect(screen,(255,255,255),self.rect)

    def update_bullet(self):
        self.y -= 5
        self.rect.y = self.y




