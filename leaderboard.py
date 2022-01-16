#LEADERBOARD MENU, COMPATIBILE WITH FIREBASE

import game_database
import pygame
from pygame.locals import *

def leaderboard_menu(screen, lboard_img, hand):
	running = True
	# Set background
	screen.fill((0, 0, 0))
	background = pygame.image.load("graphics/BG.png")
	background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
	screen.blit(background, (0, 0))

	# Get leaderboard header
	lboard_img.set_alpha(255)
	lboard_img = pygame.transform.scale(lboard_img, (700, 200))
	lboard_rect = lboard_img.get_rect(center=(640, 125))
	screen.blit(lboard_img, lboard_rect)
	pygame.display.flip()

	# Return to Main Menu Button
	back_arrow = pygame.image.load("graphics/white_arrow.png")
	back_arrow = pygame.transform.scale(back_arrow, (75, 75))
	back_arrow = pygame.transform.flip(back_arrow, True, True)
	back_rect = back_arrow.get_rect(bottomleft=(25,695))
	screen.blit(back_arrow,back_rect)
	pygame.display.update()

	# Create 5 text rects for leaderboard entries
	# Iterate through top 5 LB entries from firebase
	#font = pygame.font.SysFont(None, 48) #default
	font = pygame.font.Font("graphics/bubble.ttf", 62)

	lb_list = game_database.retrieveLeaderboard()	#list of dicts with lb entries
	height = 0
	num = 1
	for i in lb_list:
		pos = (415, 250+height) #640, 360 for center of screen
		formatted_text = f"{num}.   {i.key()}   {str(i.val()['score'])}"
		font_img = font.render(formatted_text, True, (255, 255, 255))
		rect = font_img.get_rect(topleft=pos)
		screen.blit(font_img, rect)
		height += 70
		num += 1
		pygame.display.update()

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
