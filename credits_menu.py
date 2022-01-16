#CREDITS PAGE
import pygame
from pygame.locals import *

def credits_screen(screen, bubble_font, hand):
	# Background
	background = pygame.image.load("graphics/BG.png")
	background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
	screen.blit(background, (0, 0))

	# Game devs
	credits_list = ["Eric Xiong", "Joey Quinlan", "Owen Cooke", "Zack Dorward"]
	height = 0
	for desc in credits_list:
		pos = (640, 350+height) #640, 360 for center of screen
		font_img = bubble_font.render(desc, True, (255, 255, 255))
		desc_rect = font_img.get_rect(center=pos)
		screen.blit(font_img, desc_rect)
		height += 40
		pygame.display.update()

	# Graphics desc
	credits_list = ["see project README", "Special thanks to Madilyn Orchard!"]
	height = 0
	for desc in credits_list:
		pos = (640, 575+height) #640, 360 for center of screen
		font_img = bubble_font.render(desc, True, (255, 255, 255))
		desc_rect = font_img.get_rect(center=pos)
		screen.blit(font_img, desc_rect)
		height += 40
		pygame.display.update()

	# CREDITS Title
	title = "CREDITS"
	bubble_font = pygame.font.Font("graphics/bubble.ttf", 96)
	font_img = bubble_font.render(title, True, (255, 255, 255))
	credits_rect = font_img.get_rect(center=(640, 200))
	screen.blit(font_img, credits_rect)

	# Game Dev title
	title = "Game Developers"
	bubble_font = pygame.font.Font("graphics/bubble.ttf", 48)
	font_img = bubble_font.render(title, True, (255, 255, 255))
	credits_rect = font_img.get_rect(center=(640, 300))
	screen.blit(font_img, credits_rect)

	# Madilyn's creds!
	title = "Graphics"
	bubble_font = pygame.font.Font("graphics/bubble.ttf", 48)
	font_img = bubble_font.render(title, True, (255, 255, 255))
	credits_rect = font_img.get_rect(center=(640, 525))
	screen.blit(font_img, credits_rect)


	# Return to Main Menu Button
	back_arrow = pygame.image.load("graphics/white_arrow.png")
	back_arrow = pygame.transform.scale(back_arrow, (75, 75))
	back_arrow = pygame.transform.flip(back_arrow, True, True)
	back_rect = back_arrow.get_rect(bottomleft=(25,695))
	screen.blit(back_arrow,back_rect)

	pygame.display.update()

	# Menu loop
	running = True
	while running:
		for event in pygame.event.get():
		# If user hits the x button on pygame window
			if event.type == QUIT:
				running = False
		# Return button
			pos = pygame.mouse.get_pos()
			if back_rect.collidepoint(pos):
				pygame.mouse.set_cursor(hand)
			else:
				pygame.mouse.set_cursor(*pygame.cursors.arrow)
			# If any of the buttons are clicked
			if event.type == pygame.MOUSEBUTTONDOWN:
				# Gameplay Menu
				if back_rect.collidepoint(pos):
					pygame.mouse.set_cursor(*pygame.cursors.arrow)
					return

	pygame.quit()
