import pygame.font
from Catt import Cat
from pygame.sprite import Group

class Scores():
    """вывод игровой информации"""
    def __init__(self, screen, stats):
        """инициализируем подчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (27, 31, 71)
        self.font = pygame.font.SysFont(None, 40)
        self.image_score()
        self.image_high_score()
        self.image_cats()

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (135, 206, 250))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """преобразует рекорд в графическое изображение"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (135, 206, 250))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top + 20

    def image_cats(self):
        """количество жизней"""
        self.cats = Group()
        for cat_number in range(self.stats.cats_left):
            cat = Cat(self.screen)
            cat.rect.x = 15 + cat_number * cat.rect.width
            cat.rect.y = 20
            self.cats.add(cat)

    def show_score(self):
        """вывод счет на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.cats.draw(self.screen)