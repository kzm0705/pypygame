import pygame
from pygame.locals import *
import random
import player
import enemy
import boss
import bullet
import back_ground


#初期化
pygame.init()

#設定========================

width = 450
height = 800

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
    TIMER += 1
    if TIMER > 100:
        enemy.Enemy(enemy_group,random.randint(50, 400),-10)
        TIMER = 0

#==========================================================
#インスタンス生成
player = player.Player()
boss = boss.boss()
bullet = bullet.Bullet()
bg = back_ground.Background()
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

    #Bossの当たり判定（調査中）             
    boss_hit = pygame.sprite.collide_rect(bullet, boss)
    # if boss_hit:
    #     print(boss_hit)

    boss_player_hit = pygame.sprite.collide_rect(player, boss)
    if boss_player_hit:
        print(boss_player_hit)
        player.player_life -= 1
        print(player.player_life)
        if player.player_life == 0:
            flag = False
        else:
            player.rect.x = 220
            player.rect.y = 500


    #プレイヤーの操作を反映
    pressed_key = pygame.key.get_pressed()
    player.update(pressed_key)

    #キャラクターの配置
    screen.blit(player.surf,player.rect)

    #敵の描画
    # _create_enemy()
    # enemy_group.draw(screen)
    # for ene in e\nemy_group:
    #     ene.enemy_update()

    # #bossの配置
    boss.boss_update()
    screen.blit(boss.surf,boss.rect)

    #画面の更新
    pygame.display.update()
    clock.tick(FPS)
#====================================================================================================================

pygame.quit()


