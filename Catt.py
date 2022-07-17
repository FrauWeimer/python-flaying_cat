import pygame
from pygame.sprite import Sprite

class Cat(Sprite):

    def __init__(self, screen):
        """инициализация Catt"""
        super(Cat, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("kitty.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """рисование Catt"""
        self.screen.blit(self.image, self.rect)
    def update_Catt(self):
        """обновление позиции Catt"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center +=0.5
        if self.mleft and self.rect.left > 0:
            self.center -=0.5

        self.rect.centerx = self.center

    def create_Catt(self):
        """размещает кота по центру внизу"""
        self.center = self.screen_rect.centerx
