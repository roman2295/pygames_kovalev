import pygame
from random import randint


pygame.init()
clock = pygame.time. Clock()
WIDHT = 1000
HIGHT = 600

FPS = 30

screen = pygame.display.set_mode((WIDHT, HIGHT))

run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill((randint(0, 250), randint(0, 255), randint(0, 250)))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                screen.fill((randint(0, 250), randint(0, 255), randint(0, 250)))
    pygame.display.update()

