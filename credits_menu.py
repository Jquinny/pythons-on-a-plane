#CREDITS PAGE
import pygame
from pygame.locals import *

def credits_screen(screen, bubble_font, hand):
	background = pygame.image.load("graphics/BG.png")
	background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
	screen.blit(background, (0, 0))
	pygame.display.update()