# FIXME: Fancy Header Here Later

import pygame
from pygame.locals import *
import pygame_menu

def main_menu():
	# Initialize main menu appearance
	#background = pygame.image.load("graphics/backgrounds/colored_talltrees.png")
	background = pygame.image.load("graphics/BG.png")
	background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
	plane_fly1, plane_fly2 = plane_menu_images()
	plane_rect = plane_fly1.get_rect(topright=(1500, 100)) # 1500, 100 start for moving
	screen.blit(background, (0, 0))
	pygame.display.update()
	#cloud1, cloud2, cloud3, cloud4, cloud5, cloud6 = cloud_images()
	play_img, how_img, lboard_img = button_images()
	# Main Menu loop
	running = True
	frame_flag = True
	opacity = 0
	while running:
		for event in pygame.event.get():
		# If user hits the x button on pygame window
			if event.type == QUIT:
				running = False
			# If any of the buttons are clicked
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if play_rect.collidepoint(pos):
					pygame.mouse.set_cursor(*pygame.cursors.arrow)
					pass # <-------- PUT GAMEPLAY FUNCTION HERE
				if how_rect.collidepoint(pos):
					pass # <------ PUT HOW TO PLAY MENU HERE
				if lboard_rect.collidepoint(pos):
					pass # <----- PUT LEADERBOARD MENU HERE
				if credits_rect.collidepoint(pos):
					print('credits') # <----- PUT CREDIT MENU HERE

		# Plane animation
		screen.blit(background, (0, 0))
		plane_rect, frame_flag = plane_animation(plane_rect, plane_fly1, plane_fly2, frame_flag)

		# Buttons / GUI Functionality
		play_rect = buttons(play_img, opacity, (width/2, height/2))
		how_rect = buttons(how_img, opacity, (320, 550))
		lboard_rect = buttons(lboard_img, opacity, (920, 550))
		font = pygame.font.SysFont(None, 36)
		credits = font.render("CREDITS", True, (255, 255, 255))
		credits_rect = credits.get_rect(center=(width/2, 650))
		screen.blit(credits, credits_rect)
		pygame.display.update()
		opacity += 3


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


def button_images():
	''' Loads cloud images w/ certain transparency
	cloud1 = pygame.image.load("graphics/PNG/cloud1.png")
	cloud1 = pygame.transform.scale(cloud1, (322, 151))
	cloud2 = pygame.image.load("graphics/PNG/cloud2.png")
	cloud2 = pygame.transform.scale(cloud2, (322, 151))
	cloud3 = pygame.image.load("graphics/PNG/cloud3.png")
	cloud3 = pygame.transform.scale(cloud3, (322, 151))
	cloud4 = pygame.image.load("graphics/PNG/cloud4.png")
	cloud4 = pygame.transform.scale(cloud4, (322, 151))
	cloud5 = pygame.image.load("graphics/PNG/cloud5.png")
	cloud5 = pygame.transform.scale(cloud5, (200, 85))
	cloud6 = pygame.image.load("graphics/PNG/cloud6.png")
	cloud6 = pygame.transform.scale(cloud6, (322, 151))
	return cloud1, cloud2, cloud3, cloud4, cloud5, cloud6'''
	#cloud6 = pygame.image.load("graphics/PNG/cloud6.png")
	#cloud6 = pygame.transform.scale(cloud6, (322, 151))
	play_img = pygame.image.load("graphics/play.png")
	play_img = pygame.transform.scale(play_img, (322, 151))
	how_img = pygame.image.load("graphics/howtoplay.png")
	how_img = pygame.transform.scale(how_img, (300, 200))
	lboard_img = pygame.image.load("graphics/leaderboard.png")
	lboard_img = pygame.transform.scale(lboard_img, (505, 135))
	return play_img, how_img, lboard_img #cloud6


def buttons(img, opacity, position):
	''' Adding buttons/fading in to the screen '''
	img.set_alpha(opacity)
	rect = img.get_rect(center=position)
	screen.blit(img, rect)
	return rect

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
