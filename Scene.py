import random
from config import *
import pygame


# 场景类
class Scene(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = ['./images/bg/bg1.png', './images/bg/bg2.png', './images/bg/bg3.png']
        self.x = 0
        self.bg1 = pygame.image.load(self.imgs[0]).convert_alpha()
        self.bg2 = pygame.image.load(self.imgs[1]).convert_alpha()
        self.bg3 = pygame.image.load(self.imgs[2]).convert_alpha()
        self.bg1_rect = self.bg1.get_rect()
        self.bg2_rect = self.bg2.get_rect()
        self.bg3_rect = self.bg3.get_rect()
        self.bg1_rect.left, self.bg1_rect.top = self.x, int(game_height / 2.3)
        self.bg2_rect.left, self.bg2_rect.top = self.bg1_rect.right, int(game_height / 2.3)
        self.bg3_rect.left, self.bg3_rect.top = self.bg2_rect.right, int(game_height / 2.3)

    # 不停向左移动
    def move(self):
        self.x = self.x - int(speed * speed_ratio)

    # 把自己画到屏幕上去
    def draw(self, screen):
        if self.bg1_rect.right < 0:
            self.x = self.bg1_rect.right
            self.bg1 = self.bg2
            self.bg1_rect = self.bg2_rect
            self.bg2 = self.bg3
            self.bg2_rect = self.bg3_rect
            self.bg3 = pygame.image.load(self.imgs[random.randint(0, 2)]).convert_alpha()
            self.bg3_rect = self.bg3.get_rect()
        self.bg1_rect.left, self.bg1_rect.top = self.x, int(game_height / 2.3)
        self.bg2_rect.left, self.bg2_rect.top = self.bg1_rect.right, int(game_height / 2.3)
        self.bg3_rect.left, self.bg3_rect.top = self.bg2_rect.right, int(game_height / 2.3)
        screen.blit(self.bg1, self.bg1_rect)
        screen.blit(self.bg2, self.bg2_rect)
        screen.blit(self.bg3, self.bg3_rect)
