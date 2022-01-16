# FIXME: Fancy Header Here Later

import pygame
from pygame.locals import *
import pygame_menu
import leaderboard
import random
import howtoplay

def main_menu():
	# Initialize main menu appearance
	background = pygame.image.load("graphics/BG.png")
	background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
	plane_fly1, plane_fly2 = plane_menu_images()
	plane_rect = plane_fly1.get_rect(topright=(1500, 100)) # 1500, 100 start for moving
	screen.blit(background, (0, 0))
	pygame.display.update()
	play_img, how_img, lboard_img, cursor_img = button_images()
	cursor_rect = cursor_img.get_rect()
	hand = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
	font = pygame.font.Font("graphics/bubble.ttf", 36)
	credits = font.render("CREDITS", True, (255, 255, 255))

	# Main Menu loop
	running = True
	frame_flag = True
	opacity = 0
	while running:
		# Plane animation
		screen.blit(background, (0, 0))
		plane_rect, frame_flag = plane_animation(plane_rect, plane_fly1, plane_fly2, frame_flag)

		# Buttons / GUI Functionality
		play_rect = buttons(play_img, opacity, (width/2, height/2))
		how_rect = buttons(how_img, opacity, (320, 550))
		lboard_rect = buttons(lboard_img, opacity, (920, 550))
		credits_rect = buttons(credits, opacity, (width/2, 650))
		screen.blit(credits, credits_rect)
		pygame.display.update()
		opacity += 3

		for event in pygame.event.get():
		# If user hits the x button on pygame window
			if event.type == QUIT:
				running = False
			# Hovering on buttons, change cursor icon
			pos = pygame.mouse.get_pos()
			if play_rect.collidepoint(pos) or how_rect.collidepoint(pos) or lboard_rect.collidepoint(pos) or credits_rect.collidepoint(pos):
				pygame.mouse.set_cursor(hand)
			else:
				pygame.mouse.set_cursor(*pygame.cursors.arrow)
			# If any of the buttons are clicked
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				# Gameplay Menu
				if play_rect.collidepoint(pos):
					pygame.mouse.set_cursor(*pygame.cursors.arrow)
					pass # <-------- PUT GAMEPLAY FUNCTION HERE
				# How to Play Menu
				if how_rect.collidepoint(pos):
					pygame.mouse.set_cursor(*pygame.cursors.arrow)
					howtoplay.how_menu(screen)
				# Leaderboard Menu
				if lboard_rect.collidepoint(pos):
					pygame.mouse.set_cursor(*pygame.cursors.arrow)
					leaderboard.leaderboard_menu(screen, lboard_img)
				# Credits Menu
				if credits_rect.collidepoint(pos):
					pygame.mouse.set_cursor(*pygame.cursors.arrow)
					print('credits') # <----- PUT CREDIT MENU HERE


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
	speed = [-7,0]
	# Get center position from the previous frame's rectangle
	current_center = plane_rect.center
	#current_centerx = plane_rect.centerx
	#current_centery = plane_rect.centery
	# Speed is only necessary for flying plane image across screen, not animation
	# <--- not needed for propellor animation
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
	play_img = pygame.image.load("graphics/play.png")
	play_img = pygame.transform.scale(play_img, (322, 151))
	how_img = pygame.image.load("graphics/howtoplay.png")
	how_img = pygame.transform.scale(how_img, (300, 200))
	lboard_img = pygame.image.load("graphics/leaderboard.png")
	lboard_img = pygame.transform.scale(lboard_img, (505, 135))
	cursor_img = pygame.image.load("graphics/target.png")
	cursor_img = pygame.transform.scale(cursor_img, (50, 50))
	return play_img, how_img, lboard_img, cursor_img


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
