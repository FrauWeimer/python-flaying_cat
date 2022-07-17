import pygame

class Heart(pygame.sprite.Sprite):

    def __init__(self, screen, Catt):
        """создаем сердце в позиции кота"""
        super(Heart, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 30, 12)
        self.color = 213, 0, 0
        self.speed = 0.5
        self.rect.centerx = Catt.rect.centerx
        self.rect.top = Catt.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение сердца вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_heart(self):
        """рисуем сердце на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)