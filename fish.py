import pygame

class Fish(pygame.sprite.Sprite):
    """класс одной рыбы"""

    def __init__(self, screen):
       """инициализируем и заадем начальную позицию"""
       super(Fish, self).__init__()
       self.screen = screen
       self.image = pygame.image.load("fish.png")
       self.rect = self.image.get_rect()
       self.rect.x = self.rect.width
       self.rect.y = self.rect.height
       self.x = float(self.rect.x)
       self.y = float(self.rect.y)

    def draw(self):
        """вывод рыбы на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещение рыб"""
        self.y += 0.03
        self.rect.y = self.y