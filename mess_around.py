# FIXME: Fancy Header Here Later

import pygame
import random
import background
import obstacles
from pygame.locals import *

pygame.init()

# CONSTANT values like colours here
#SKYBLUE = (135, 206, 235)

# Create vars for screen size and width/height of screen
size = (1280, 720)
width, height = size
clouds = ["cloud1", "cloud5", "cloud9"] # ----------------------------------------------- my important variables ---------------------------
ground_obstacles = ["grey house", "tree"]

# set a screen variable
screen = pygame.display.set_mode(size)

backgrounds = pygame.sprite.Group()
ground_objs = pygame.sprite.Group()

sky_surf = pygame.image.load("graphics/backgrounds/uncolored_hills.png").convert()
sky_surf_scaled = pygame.transform.scale(sky_surf, (1280,720))
clock = pygame.time.Clock()

cloud_timer = pygame.USEREVENT + 1
pygame.time.set_timer(cloud_timer, 3000)

ground_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ground_timer, 2000) # -------------------------------------------------------------------------------------------------

font = pygame.font.Font(None, 50)
start_time = 0
def score():
    current_time = pygame.time.get_ticks() - start_time
    time = str(current_time/1000)
    score_surf = font.render(time, False, (64, 64, 64))
    score_rect = score_surf.get_rect(topleft = (0,0))
    screen.blit(score_surf, score_rect)

# Main game loop
running = True
while running:
	# Event loop (for KEYDOWN, etc.)
    for event in pygame.event.get():
    	# If user hits the x button on pygame window
        if event.type == QUIT:
            running = False
        
        if event.type == cloud_timer:
            backgrounds.add(background.Background(clouds[random.randint(0,2)]))

        if event.type == ground_timer:
            ground_objs.add(obstacles.GroundObstacles(ground_obstacles[random.randint(0,1)]))
    
    screen.blit(sky_surf_scaled, (0,0))

    backgrounds.draw(screen)
    ground_objs.draw(screen)
    backgrounds.update()
    ground_objs.update()
    score()
    pygame.display.update()
    clock.tick(60)

pygame.quit()