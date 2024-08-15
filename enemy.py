import pygame
import random

width = 450
height = 600


class Enemy(pygame.sprite.Sprite):
    def __init__(self,groups,x,y):
       super().__init__(groups)

       #画像
       self.image = pygame.image.load('pypygame/source/png/enemy.png')
       self.rect = self.image.get_rect(center= (x,y))

       #移動
       move_list = [1,-1]
       self.direction = pygame.math.Vector2((random.choice(move_list),1))
       self.speed  = 1
       self.timer = 0


#敵を移動させる
    def move_enemy(self):
        self.timer += 1
        if self.timer > 80:
            self.direction.x *= -1
            self.timer = 0
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def enemy_update(self):
        self.move_enemy()











