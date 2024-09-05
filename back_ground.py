import pygame
from pygame.locals import *

height = 800

class Background():
    def __init__(self):
        self.image = pygame.image.load("pypygame/source/png/back_ground_space.png")
        #スクロールスピード
        self.scroll_speed = 1
        #スクロール用のY座標
        self.bgy = 0
        

    #スクロールさせる関数
    def scroll_bg(self,screen):
        self.bgy = (self.bgy + self.scroll_speed ) % height
        screen.blit(self.image,[0,self.bgy-height])
        screen.blit(self.image,[0,self.bgy])