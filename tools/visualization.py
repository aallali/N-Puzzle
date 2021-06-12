import pygame
from pygame.locals import *
import time

BLACK = (216, 227, 231)
BG = (250, 243, 243)
WHITE = (37, 150, 190)
TILE = (37, 150, 190)
SIZE =  20


def draw_tile(screen, x, y, color, full):
	size = 	SIZE
	rect = Rect(x, y, size, size)
	if full:
		pygame.draw.rect(screen, TILE, rect)
	pygame.draw.rect(screen, BLACK, rect, 3)


def draw_state(screen, posx, posy, dim, puzzle):
	size = SIZE
	x = posx
	y = posy

	font = pygame.font.SysFont(None, 30)
	for item in puzzle:
		if item != 0:
			draw_tile(screen, x, y, BLACK, 1)
		else:
			draw_tile(screen, x, y, BG, 0)
		if item != 0:
			img = font.render(str(item), True, BLACK)
			screen.blit(img, (x + (SIZE/2)-5, y + (SIZE/2)-5))

		if (puzzle.index(item) + 1) % dim == 0:
			x = posx
			y += size
		else:
			x += size
	pygame.display.update()


def visualize(array, dim):
	global SIZE
	wait = 0
	if dim == 3:
		wait = 0.3
	elif dim == 4:
		wait = 0.1
	else:
		wait = 0.05
	SIZE = 60 + dim * SIZE
	x = dim * SIZE + 10

	pygame.init()

	posx = x / 2 - (SIZE / 2) * dim
	posy = x / 2 - (SIZE / 2) * dim

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
