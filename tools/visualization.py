

import pygame
from pygame.locals import *
import time

BLACK = (216, 227, 231)
BG = (250, 243, 243)
WHITE = (37, 150, 190)
TILE = (37, 150, 190)



def draw_tile(screen, x, y, color, full):
    size = 100
    rect = Rect(x, y, size, size)
    if full:
        pygame.draw.rect(screen, TILE, rect)
    pygame.draw.rect(screen, BLACK, rect, 3)


def draw_state(screen, posx, posy, dim, puzzle):
    size = 100
    x = posx
    y = posy

    font = pygame.font.SysFont(None, 50)
    for item in puzzle:
        if item != 0:
            draw_tile(screen, x, y, BLACK, 1)
        else:
            draw_tile(screen, x, y, BG, 0)
        if item != 0:
            img = font.render(str(item), True, BLACK)
            screen.blit(img, (x + 42, y + 42))

        if (puzzle.index(item) + 1) % dim == 0:
            x = posx
            y += size
        else:
            x += size
    pygame.display.update()


def visualize(array, dim):
    wait = 0
    if dim == 3:
        wait = 0.1
    elif dim == 4:
        wait = 0.08
    else:
        wait = 0.05
    x = dim * 100 + 10
    pygame.init()


    posx = x / 2 - (100 / 2) * dim
    posy = x / 2 - (100 / 2) * dim

    screen = pygame.display.set_mode((x, x))

    running = True
    start = 2
    while running:
        screen.fill(BG)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == 13:
                    start = 1

        if start == 2:
            draw_state(screen, posx, posy, dim, array[0])
        elif start == 1:
            for puzzle in array:
                draw_state(screen, posx, posy, dim, puzzle)
                screen.fill(BG)
                time.sleep(wait)
                start = 0
    pygame.quit()
