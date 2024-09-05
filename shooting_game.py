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
TIMER2 = 0
TIMER3 = 0
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width,height))
screen_name = pygame.display.set_caption('スペースシューティングゲーム')


#関数
# def fire_bullet():
#     new_bullet = bullet.bullet()
#     bullets_group.add(new_bullet)

def _create_enemy1():
    global TIMER
    TIMER += 1
<<<<<<< Updated upstream
    if TIMER > 50:
        print(TIMER)
        Enemy(enemy_group,220,100)
=======
    if TIMER > 100:
        enemy.Enemy(enemy_group1,random.randint(50, 400),-10)
>>>>>>> Stashed changes
        TIMER = 0
def _create_enemy2():
    global TIMER2
    TIMER2 += 1
    if TIMER2 > 150:
        x = enemy.Enemy(enemy_group1,random.randint(50,400),-10)
        enemy_group2.add(x)
        TIMER2 = 0
def _create_enemy3():
    global TIMER3
    TIMER3 += 1
    if TIMER3 > 150:
        x = enemy.Enemy(enemy_group1,-15,random.randint(50,500))
        enemy_group3.add(x)
        TIMER3 = 0





#==========================================================
#インスタンス生成
player = player.Player()
boss = boss.boss()
bg = back_ground.Background()
<<<<<<< Updated upstream
bullets_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy = Enemy(220,100)
=======
enemy_group1 = pygame.sprite.Group()
enemy_group2 = pygame.sprite.Group()
enemy_group3 = pygame.sprite.Group()
score = ui.Userinterface()


>>>>>>> Stashed changes
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
                

    pressed_key = pygame.key.get_pressed()
    player.update(pressed_key)

    #キャラクターの配置
    screen.blit(player.surf,player.rect)

    #敵の描画
<<<<<<< Updated upstream
    enemy_group.draw(screen)
    Enemy.enemy_update()
    # #bossの配置
    # boss.boss_update()
    # screen.blit(boss.surf,boss.rect)
=======
    _create_enemy1()
    _create_enemy2()
    _create_enemy3()
    enemy_group1.draw(screen)
    enemy_group2.draw(screen)
    enemy_group3.draw(screen)
    # print(enemy_group1.sprites())
    # print(enemy_group2.sprites())
    for ene in enemy_group1:
        if ene in enemy_group2:
            ene.move_2()
        elif ene in enemy_group3:
            ene.move_3()
        elif ene in enemy_group1:
            ene.move_1()
        
        
    # #bossの配置
    # boss.boss_update()
    # screen.blit(boss.surf,boss.rect)

>>>>>>> Stashed changes

    #画面の更新
    pygame.display.update()
    clock.tick(FPS)
#====================================================================================================================

pygame.quit()



