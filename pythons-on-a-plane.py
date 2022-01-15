# FIXME: Fancy Header Here Later

import pygame
from pygame.locals import *

# CONSTANT values like colours here
SKYBLUE = (135, 206, 235)

# Create vars for screen size and width/height of screen
size = (1280, 720)
width, height = size

# Initialize pygame and set a screen variable
pygame.init()
screen = pygame.display.set_mode(size)

# Main game loop
running = True
while running:
	# Event loop (for KEYDOWN, etc.)
    for event in pygame.event.get():
    	# If user hits the x button on pygame window
        if event.type == QUIT:
            running = False

pygame.quit()
