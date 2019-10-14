import random
from config import *
import pygame


# 植物
class Plant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 统计分数时用的
        self.added_score = False
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
        self.rect.left, self.rect.top = game_width + 60, int(game_height / 2)

    # 不停往左移动
    def move(self):
        self.rect.left = self.rect.left - int(speed * speed_ratio)

    # 把自己画到屏幕上去
    def draw(self, screen):
        screen.blit(self.plant, self.rect)
