# FIXME: Fancy Header Here Later

import pygame
import random
import background
from pygame.locals import *

pygame.init()

# CONSTANT values like colours here
#SKYBLUE = (135, 206, 235)

# Create vars for screen size and width/height of screen
size = (1280, 720)
width, height = size
clouds = ["cloud1", "cloud5", "cloud9"]

# set a screen variable
screen = pygame.display.set_mode(size)

backgrounds = pygame.sprite.Group()

sky_surf = pygame.image.load("graphics/BG.png").convert()
clock = pygame.time.Clock()
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 3000)

# Main game loop
running = True
while running:
	# Event loop (for KEYDOWN, etc.)
    for event in pygame.event.get():
    	# If user hits the x button on pygame window
        if event.type == QUIT:
            running = False
        
        if event.type == timer:
            backgrounds.add(background.Background(clouds[random.randint(0,2)]))
    
    screen.blit(sky_surf, (0,0))

    backgrounds.draw(screen)
    backgrounds.update()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()