import pygame, controls
from Catt import Cat
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Flying cat")
    bg_color = (135, 206, 250)
    Catt = Cat(screen)
    hearts = Group()
    fishes = Group()
    controls.create_army(screen, fishes)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, Catt, hearts)
        if stats.run_game:
            Catt.update_Catt()
            controls.update(bg_color, screen, stats, sc, Catt, fishes, hearts)
            controls.update_hearts(screen, stats, sc, fishes, hearts)
            controls.update_fishes(stats, screen, sc, Catt, fishes, hearts)

run()