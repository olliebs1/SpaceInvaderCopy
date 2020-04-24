import pygame
import os
import time
import random


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
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()
