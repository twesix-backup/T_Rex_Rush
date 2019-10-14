import pygame
from config import *


# 恐龙类
class Dino(pygame.sprite.Sprite):
    def __init__(self, width=640, height=500):
        pygame.sprite.Sprite.__init__(self)

        self.HEIGHT = height
        self.WIDTH = width
        self.dinosaur_size = (88, 95)
        self.status_stop = (88 * 4, 0)
        self.status_running_1 = (88 * 2, 0)
        self.status_running_2 = (88 * 3, 0)
        self.dinosaurs = pygame.image.load('./images/dinosaur/dino.png').convert_alpha()
        self.dinosaur_stop = self.dinosaurs.subsurface(self.status_stop, self.dinosaur_size)
        self.dinosaur_running_1 = self.dinosaurs.subsurface(self.status_running_1, self.dinosaur_size)
        self.dinosaur_running_2 = self.dinosaurs.subsurface(self.status_running_2, self.dinosaur_size)

        # 恐龙是否在奔跑
        self.is_running = False
        # 为了奔跑特效
        self.running_flag = False
        self.running_count = 0
        # 恐龙是否在跳跃
        self.is_jumping = False
        # 恐龙是否在向上跳跃
        self.is_jumping_up = True
        # 跳跃初始速度
        self.jump_initial_speed = 1200
        # 跳跃瞬时速度
        self.jump_v = self.jump_initial_speed
        # 跳跃加速度
        self.jump_acceleration = 5000
        # 小恐龙初始位置
        self.initial_left = 40
        self.initial_top = int(self.HEIGHT / 2.3)

        self.dinosaur = self.dinosaur_stop
        self.rect = self.dinosaur.get_rect()
        self.rect.left, self.rect.top = self.initial_left, self.initial_top
        print(self.rect)

    # 跳跃
    def jump(self, time_passed):
        # time_passed很小时，可近似为匀速运动
        if self.is_jumping_up:
            self.rect.top -= self.jump_v * time_passed
            self.jump_v = max(0, self.jump_v - self.jump_acceleration * time_passed)
            if self.jump_v == 0:
                self.is_jumping_up = False
        else:
            self.rect.top = min(self.initial_top, self.rect.top + self.jump_v * time_passed)
            self.jump_v += self.jump_acceleration * time_passed
            if self.rect.top == self.initial_top:
                self.is_jumping = False
                self.is_jumping_up = True
                self.jump_v = self.jump_initial_speed

    # 把自己画到屏幕上去
    def draw(self, screen):
        if self.is_running and not self.is_jumping:
            self.running_count += 1
            if self.running_count == 6:
                self.running_count = 0
                self.running_flag = not self.running_flag
            if self.running_flag:
                self.dinosaur = self.dinosaur_running_1
            else:
                self.dinosaur = self.dinosaur_running_2
        screen.blit(self.dinosaur, self.rect)
