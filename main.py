import pygame
import os
import time
import random
pygame.font.init()


Width, Height = 750, 750
WIN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Space Invaders Copy')

# Ships
redSpaceShip = pygame.image.load(
    os.path.join('assets', 'pixel_ship_red_small.png'))

greenSpaceShip = pygame.image.load(
    os.path.join('assets', 'pixel_ship_green_small.png'))

blueSpaceShip = pygame.image.load(
    os.path.join('assets', 'pixel_ship_blue_small.png'))

# Player Ship
yellowSpaceShip = pygame.image.load(
    os.path.join('assets', 'pixel_ship_yellow.png'))

# Lasers
redLaser = pygame.image.load(
    os.path.join('assets', 'pixel_laser_red.png'))

greenLaser = pygame.image.load(
    os.path.join('assets', 'pixel_laser_green.png'))

blueLaser = pygame.image.load(
    os.path.join('assets', 'pixel_laser_blue.png'))

yellowLaser = pygame.image.load(
    os.path.join('assets', 'pixel_laser_yellow.png'))

# Background

BG = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'background-black.png')), (Width, Height))


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont('comicsans', 50)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
        level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (Width - level_label.get_width() - 10, 10))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()
