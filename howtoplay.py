#howtoplay.py

import pygame
from pygame.locals import *

def how_menu(screen, how_img, bubble_font, hand):
	# Background
	background = pygame.image.load("graphics/BG.png")
	background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
	screen.blit(background, (0, 0))

	# How to Play title
	how_img = pygame.transform.scale(how_img, (425, 300))
	how_img.set_alpha(255)
	how_rect = how_img.get_rect(centerx=640)
	screen.blit(how_img, how_rect)
	pygame.display.update()

	# How to Play Instructions
	instructions = "Dodge pipes and falling objects! Shoot your enemies!"
	font_img = bubble_font.render(instructions, True, (255, 255, 255))
	inst_rect = font_img.get_rect(center=(640, 350))
	screen.blit(font_img, inst_rect)
	pygame.display.update()

	# Button Controls
	move = "Move with WASD or Arrow Keys"
	shoot = "Click to Shoot"
	font_img = bubble_font.render(move, True, (255, 255, 255))
	move_rect = font_img.get_rect(center=(640,450))
	screen.blit(font_img, move_rect)
	font_img = bubble_font.render(shoot, True, (255, 255, 255))
	shoot_rect = font_img.get_rect(center=(640,550))
	screen.blit(font_img, shoot_rect)
	pygame.display.update()

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
