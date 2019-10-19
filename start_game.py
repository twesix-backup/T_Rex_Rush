import math
import random
import sys
import time

import pygame
from pygame.locals import *

from Dino import Dino
from Obstacle import Plant
from Scene import Scene
from config import *


# 显示Gameover界面
def show_gameover(screen):
    screen.fill(BACKGROUND_COLOR)
    gameover_img = pygame.image.load('./images/others/gameover.png').convert_alpha()
    gameover_rect = gameover_img.get_rect()
    gameover_rect.left, gameover_rect.top = (game_width - gameover_width) // 2, game_height // 2 - gameover_height
    screen.blit(gameover_img, gameover_rect)
    restart_img = pygame.image.load('./images/others/restart.png').convert_alpha()
    restart_rect = restart_img.get_rect()
    restart_rect.left, restart_rect.top = (game_width - game_restart_width) // 2, game_height // 1.5 - game_restart_height
    screen.blit(restart_img, restart_rect)
    pygame.display.update()

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if restart_rect.right > mouse_pos[0] > restart_rect.left and \
                        restart_rect.bottom > mouse_pos[1] > restart_rect.top:
                    return True

        # key_pressed = pygame.key.get_pressed()
        # if key_pressed[pygame.K_SPACE]:
        #     return True


# 将Score转为生成障碍物的概率
def sigmoid(score):
    probability = 1 / (1 + math.exp(-score))
    return min(probability, 0.6)


# 主函数
def main():

    # 初始化
    pygame.init()
    screen = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption("T-Rex Rush")
    clock = pygame.time.Clock()

    # 得分
    score = 0

    # 加载一些素材
    jump_sound = pygame.mixer.Sound("./music/jump.wav")
    jump_sound.set_volume(6)
    die_sound = pygame.mixer.Sound("./music/die.wav")
    die_sound.set_volume(6)
    pygame.mixer.init()
    pygame.mixer.music.load("./music/bg_music.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
    font = pygame.font.Font('./font/simkai.ttf', 20)
    # 实例化
    dinosaur = Dino(game_width, game_height)
    scene = Scene()
    plants = pygame.sprite.Group()

    # 产生障碍物事件
    GenPlantEvent = pygame.constants.USEREVENT + 0
    pygame.time.set_timer(GenPlantEvent, random.randint(300, 1000))

    # 游戏是否结束了
    running = True

    # 是否可以产生障碍物flag
    flag_plant = False

    t0 = time.time()
    # 主循环
    while running:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == GenPlantEvent:
                flag_plant = True

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]:
            dinosaur.is_jumping = True
            jump_sound.play()

        screen.fill(BACKGROUND_COLOR)
        time_passed = time.time() - t0
        t0 = time.time()

        # 场景
        scene.move()
        scene.draw(screen)

        # 小恐龙
        dinosaur.is_running = True
        if dinosaur.is_jumping:
            dinosaur.jump(time_passed)
        dinosaur.draw(screen)

        # 障碍物-植物
        if random.random() < sigmoid(score) and flag_plant:
            plant = Plant()
            plants.add(plant)
            flag_plant = False
        for plant in plants:
            plant.move()
            if dinosaur.rect.left > plant.rect.right and not plant.added_score:
                score += 1
                set_speed_ratio(1 + (score // 5) * 0.1)
                plant.added_score = True
            if plant.rect.right < 0:
                plants.remove(plant)
                continue
            plant.draw(screen)

        # 碰撞检测
        for plant in plants:
            if pygame.sprite.collide_rect_ratio(0.7)(dinosaur, plant):
                die_sound.play()
                running = False

        score_text = font.render("Score: " + str(score) + ", Speed Ratio: " + str(get_speed_ratio()), 1, (0, 0, 0))
        screen.blit(score_text, [10, 10])
        pygame.display.flip()
        clock.tick(300)

    return show_gameover(screen)


if __name__ == '__main__':
    res = True
    while res:
        res = main()
