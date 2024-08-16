import pygame
from pygame.locals import *
import player
import enemy
import boss
import bullet
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

width = 450
height = 800
bullet_speed = 5

class Player(pygame.sprite.Sprite):
    player_life = 0

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("pypygame/source/png/player.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(width-220, height-50))
        self.player_life = 3

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
            # move_up_sound.play()
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
            # move_down_sound.play()
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height 

    def fire_bullet(self, screen):
        fired_bullet = bullet.Bullet()
        current_player_rect_x = self.rect.centerx
        current_player_rect_y = self.rect.centery
        fired_bullet.update_bullet(current_player_rect_x, current_player_rect_y, screen)
            