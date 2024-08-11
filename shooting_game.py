import pygame
from pygame.locals import *
import player
import enemy
import boss
import back_ground

#初期化
pygame.init()

#設定

width = 450
height = 600

RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width,height))
screen_name = pygame.display.set_caption('スペースシューティングゲーム')

player = player.player()
enemy = enemy.enemy()
boss = boss.boss()
bg = back_ground.Background()

#メインループ===============================================================================================================
flag  =True
while flag:

    #イベントの取得
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                flag = False

    pressed_key = pygame.key.get_pressed()
    player.update(pressed_key)
    bg.scroll_bg(screen)

    #キャラクターの配置
    screen.blit(player.surf,player.rect)
    
    #画面の更新
    pygame.display.update()
    clock.tick(FPS)
#====================================================================================================================

pygame.quit()




