import random
from config import *
import pygame


# 植物
class Plant(pygame.sprite.Sprite):
    def __init__(self, width=640, height=500):
        pygame.sprite.Sprite.__init__(self)
        self.WIDTH = width
        self.HEIGHT = height
        # 统计分数时用的
        self.added_score = False
        self.speed = 10
        self.imgs = ['./images/obstacles/plant_big.png', './images/obstacles/plant_small.png']
        idx = random.randint(0, 1)
        temp = pygame.image.load(self.imgs[idx]).convert_alpha()
        if idx == 0:
            size = 101
            self.plant = temp.subsurface((size * random.randint(0, 2), 0), (size, size))
        else:
            size = 68
            self.plant = temp.subsurface((size * random.randint(0, 2), 0), (size, size))
        self.rect = self.plant.get_rect()
        self.rect.left, self.rect.top = self.WIDTH + 60, int(self.HEIGHT / 2)

    # 不停往左移动
    def move(self):
        self.rect.left = self.rect.left - self.speed

    # 把自己画到屏幕上去
    def draw(self, screen):
        screen.blit(self.plant, self.rect)


# 飞龙
class Ptera(pygame.sprite.Sprite):
    def __init__(self, height=640, width=500):
        pygame.sprite.Sprite.__init__(self)
        self.WIDTH = height
        self.HEIGHT = width
        # 统计分数时用的
        self.added_score = False
        # 为了飞行特效
        self.flying_count = 0
        self.flying_flag = True
        # 统计分数时用的
        self.speed = 12
        self.ptera = pygame.image.load('./images/obstacles/ptera.png').convert_alpha()
        self.ptera_0 = self.ptera.subsurface((0, 0), (92, 81))
        self.ptera_1 = self.ptera.subsurface((92, 0), (92, 81))
        self.rect = self.ptera_0.get_rect()
        self.rect.left, self.rect.top = self.WIDTH + 30, int(self.HEIGHT / 2) - dino_height * 1.2

    # 不停往左移动
    def move(self):
        self.rect.left = self.rect.left - self.speed

    # 把自己画到屏幕上去
    def draw(self, screen):
        self.flying_count += 1
        if self.flying_count % 6 == 0:
            self.flying_flag = not self.flying_flag
        if self.flying_flag:
            screen.blit(self.ptera_0, self.rect)
        else:
            screen.blit(self.ptera_1, self.rect)
