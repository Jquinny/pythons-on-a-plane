#howtoplay.py

import pygame
from pygame.locals import *

def how_menu(screen):
	background = pygame.image.load("graphics/BG.png")
	background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
	screen.blit(background, (0, 0))
	pygame.display.update()
	running = True
	while running:
		for event in pygame.event.get():
		# If user hits the x button on pygame window
			if event.type == QUIT:
				running = False
	pygame.quit()
