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
ground_obstacles = ["ground obj 1", "ground obj 2", "ground obj 3"]
air_obstacles = ["asteroid", "anvil"]

# set a screen variable
screen = pygame.display.set_mode(size)

backgrounds = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
air_group = pygame.sprite.Group()

sky_surf = pygame.image.load("graphics/backgrounds/uncolored_hills.png").convert()
sky_surf_scaled = pygame.transform.scale(sky_surf, (1280,720))

clock = pygame.time.Clock()
air_time = 0
cloud_time = 0
ground_time = 0

air_speed = 180
ground_speed = 420

frame_counter = 0
checker = True

font = pygame.font.Font(None, 50)
start_time = 0
def score():
    current_time = pygame.time.get_ticks() - start_time
    time = str(current_time/1000)
    score_surf = font.render(time, False, (64, 64, 64))
    score_rect = score_surf.get_rect(topleft = (0,0))
    screen.blit(score_surf, score_rect) # -------------------------------------------------------------------------------------------------

# Main game loop
running = True
while running:
	# Event loop (for KEYDOWN, etc.)
    for event in pygame.event.get():
    	# If user hits the x button on pygame window
        if event.type == QUIT:
            running = False

    screen.blit(sky_surf_scaled, (0,0))

    ground_time += 1
    air_time += 1
    cloud_time += 1
    frame_counter += 1
    
    if (frame_counter > 300) and (checker == True):
        air_speed -= 2
        ground_speed -= 5
        frame_counter = 0
        if (air_speed < 120) or (ground_speed < 180):
            checker = False

    if (air_time > air_speed):
        obj2 = random.randint(0,1)
        x = random.randint(400, 1280)
        slope = random.randint(1,8)
        air_group.add(obstacles.AirObstacles(air_obstacles[obj2], x, slope))
        air_time = 0
    
    if (cloud_time > 180):
        backgrounds.add(background.Background(clouds[random.randint(0,2)]))
        cloud_time = 0

    if (ground_time > ground_speed):
        ground_group.add(obstacles.GroundObstacles(ground_obstacles[random.randint(0,2)]))
        ground_time = 0

    backgrounds.draw(screen)
    backgrounds.update()

    ground_group.draw(screen)
    ground_group.update()

    air_group.draw(screen)
    air_group.update()

    score()
    pygame.display.update()
    clock.tick(60)

air_group.empty()
ground_group.empty()
pygame.quit()