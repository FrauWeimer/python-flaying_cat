import pygame, sys
from heart import Heart
from fish import Fish
import time

def events(screen, Catt, hearts):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_RIGHT:
                Catt.mright = True
            elif event.key == pygame.K_LEFT:
                Catt.mleft = True
            elif event.key == pygame.K_SPACE:
                new_heart = Heart(screen, Catt)
                hearts.add(new_heart)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_RIGHT:
                Catt.mright = False
            elif event.key == pygame.K_LEFT:
                Catt.mleft = False

def update(bg_color, screen, stats, sc, Catt, fishes, hearts):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for heart in hearts.sprites():
        heart.draw_heart()
    Catt.output()
    fishes.draw(screen)
    pygame.display.flip()

def update_hearts(screen, stats, sc, fishes, hearts):
    """обновлять позиции сердец"""
    hearts.update()
    for heart in hearts.copy():
        if heart.rect.bottom <=0:
            hearts.remove(heart)
    collisions = pygame.sprite.groupcollide(hearts, fishes, True, True)
    if collisions:
        stats.score += 1
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_cats()
    if len(fishes) == 0:
        hearts.empty()
        create_army(screen, fishes)


def Catt_kill(stats, screen, sc, Catt, fishes, hearts):
    """столкноваение кота и рыб"""
    if stats.cats_left > 0:
        stats.cats_left -= 1
        sc.image_cats()
        fishes.empty()
        hearts.empty()
        create_army(screen, fishes)
        Catt.create_Catt()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def update_fishes(stats, screen, sc, Catt, fishes, hearts):
    """обновляет позицию рыб"""
    fishes.update()
    if pygame.sprite.spritecollideany (Catt, fishes):
        Catt_kill(stats, screen, sc, Catt, fishes, hearts)
    fishes_check(stats, screen, sc, Catt, fishes, hearts)

def fishes_check(stats, screen, sc, Catt, fishes, hearts):
    """проверка, добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for fish in fishes.sprites():
        if fish.rect.bottom >= screen_rect.bottom:
            Catt_kill(stats, screen, sc, Catt, fishes, hearts)
            break


def create_army(screen, fishes):
    """создание армии рыб"""
    fish = Fish(screen)
    fish_width = fish.rect.width
    number_fish_x = int((700 - 2 * fish_width) / fish_width)
    fish_height = fish.rect.height
    number_fish_y = int((600 - 150 - 2 * fish_height) / fish_height)

    for row_number in range(number_fish_y - 1):
        for fish_number in range(number_fish_x):
            fish = Fish(screen)
            fish.x = fish_width + (fish_width * fish_number)
            fish.y = fish_height + (fish_height * row_number)
            fish.rect.x = fish.x
            fish.rect.y = fish.rect.height + (fish.rect.height * row_number)
            fishes.add(fish)

def check_high_score(stats, sc):
        """проверка новых рекордов"""
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sc.image_high_score()
            with open ("highscore.txt", "w") as f:
                f.write(str(stats.high_score))