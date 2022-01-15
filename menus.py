# FIXME: Fancy Header Here Later

import pygame
from pygame.locals import *

def main_menu():
	# Initialize main menu appearance
	#SKYBLUE = (135, 206, 235)
	#screen.fill(SKYBLUE)
	background = pygame.image.load("graphics/backgrounds/colored_talltrees.png")
	background = pygame.transform.scale(background, (1280, 1280))
	plane_fly1, plane_fly2 = plane_menu_images()
	plane_rect = plane_fly1.get_rect(topright=(1500, 100)) # 1500, 100 start for moving
	screen.blit(background, (0, 0))
	pygame.display.update()

	# Main Menu loop
	running = True
	frame_flag = True
	while running:
		for event in pygame.event.get():
		# If user hits the x button on pygame window
			if event.type == QUIT:
				running = False
		screen.blit(background, (0, 0))
		plane_rect, frame_flag = plane_animation(plane_rect, plane_fly1, plane_fly2, frame_flag)
		pygame.display.update()


def plane_menu_images():
	''' Loads plane images and returns them after manipulation '''

	# Loading, scaling and flipping first plane image
	plane_fly1 = pygame.image.load("graphics/plane/Fly (1).png")
	plane_fly1 = pygame.transform.scale(plane_fly1, (222, 151))
	plane_fly1 = pygame.transform.flip(plane_fly1, True, False)
	# Loading, scaling and flipping second plane image
	plane_fly2 = pygame.image.load("graphics/plane/Fly (2).png")
	plane_fly2 = pygame.transform.scale(plane_fly2, (222, 151))
	plane_fly2 = pygame.transform.flip(plane_fly2, True, False)
	# Returns two pygame images
	return plane_fly1, plane_fly2


def plane_animation(plane_rect, plane_fly1, plane_fly2, frame_flag):
	''' Creates animation for plane's propellor.
	Also some functionality for menu movement.
	NOTE: be sure to call screen.blit(background, (0, 0)) before this function '''

	# Get center position from the previous frame's rectangle
	current_center = plane_rect.center
	# Speed is only necessary for flying plane image across screen, not animation
	speed = [-5,0]	# <--- not needed for propellor animation
	# Alternate images every frame
	if frame_flag:
		# Create a new rect with alternate plane image
		# *** At same location as previous frame using "center ="
		plane_rect = plane_fly2.get_rect(center = current_center)
		plane_rect = plane_rect.move(speed) # <--- not needed for propellor animation
		screen.blit(plane_fly2, plane_rect)
	else:
		plane_rect = plane_fly1.get_rect(center = current_center)
		plane_rect = plane_rect.move(speed) # <--- not needed for propellor animation
		screen.blit(plane_fly1, plane_rect)
	frame_flag = not frame_flag
	return plane_rect, frame_flag


if __name__ == "__main__":
	# CONSTANT values like colours here
	SKYBLUE = (135, 206, 235)

	# Create vars for screen size and width/height of screen
	size = 1280, 720
	width, height = size

	# Initialize pygame and set a screen variable
	pygame.init()
	screen = pygame.display.set_mode(size)

	# Main game loop
	main_menu()

	pygame.quit()
