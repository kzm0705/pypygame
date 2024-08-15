import pygame
from pygame.locals import *
import player
from enemy import Enemy 
import boss
import bullet
import back_ground

#初期化
pygame.init()

#設定========================

width = 450
height = 600

RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 60

TIMER = 0
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width,height))
screen_name = pygame.display.set_caption('スペースシューティングゲーム')


#関数
# def fire_bullet():
#     new_bullet = bullet.bullet()
#     bullets_group.add(new_bullet)

def _create_enemy():
    global TIMER 
    enemy = Enemy(enemy_group,220,100)
    TIMER += 1
    if TIMER > 50:
        Enemy(enemy_group,220,100)
        TIMER = 0

#==========================================================
#インスタンス生成
player = player.Player()
boss = boss.boss()
bullet = bullet.Bullet()
bg = back_ground.Background()
bullets_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

#メインループ===============================================================================================================
flag  =True
while flag:
    #スクロールするスクリーンの背景を描画
    bg.scroll_bg(screen)
    #イベントの取得
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                flag = False
            if event.key == pygame.K_SPACE:
                player.fire_bullet(screen)


    #弾とボスの当たり判定
    if(pygame.sprite.collide_rect(bullet, boss)):
        print("hit")
        boss.boss_HP -= 10
        if(boss.boss_HP == 0):
            boss.sprite.remove()
            

    pressed_key = pygame.key.get_pressed()
    player.update(pressed_key)

    #キャラクターの配置
    screen.blit(player.surf,player.rect)

    #敵の描画
    _create_enemy()
    enemy_group.draw(screen)
    enemy_group.enemy_update()
    # #bossの配置
    # boss.boss_update()
    # screen.blit(boss.surf,boss.rect)

    #画面の更新
    pygame.display.update()
    clock.tick(FPS)
#====================================================================================================================

pygame.quit()



