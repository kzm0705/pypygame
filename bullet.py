import pygame
from pygame.sprite import Sprite
from pygame.locals import *
import player
import enemy
import boss

#Spriteクラスを継承する、Spriteで弾を管理する
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #長方形の弾を作る(x軸,y軸,width,height)
        self.rect = pygame.Rect(230,550,5,50)
        #弾のｙ座標を浮動小数点数にする
        self.y = float(self.rect.y)

    def draw_bullet(self,screen,):
        #self.rect.left = x
        #self.rect.top = y
        pygame.draw.rect(screen,(255,255,255),self.rect)

    def update_bullet(self):
        self.y -= 5
        self.rect.y = self.y



