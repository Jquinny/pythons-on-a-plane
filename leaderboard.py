#LEADERBOARD MENU, COMPATIBILE WITH FIREBASE

import game_database
import pygame
from pygame.locals import *

def leaderboard_menu(screen, lboard_img):
	running = True
	# Set background
	screen.fill((0, 0, 0))
	background = pygame.image.load("graphics/BG.png")
	background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
	screen.blit(background, (0, 0))

	# Get leaderboard header
	lboard_img.set_alpha(255)
	lboard_rect = lboard_img.get_rect()
	screen.blit(lboard_img, lboard_rect)
	pygame.display.flip()
	#print(pygame.font.get_fonts())
	# Create 5 text rects for leaderboard entries
	# Iterate through top 5 LB entries from firebase
	#font = pygame.font.SysFont(None, 48) #default
	font = pygame.font.Font("graphics/bubble.ttf", 62)

	lb_list = game_database.retrieveLeaderboard()	#list of dicts with lb entries
	height = 0
	num = 1
	for i in lb_list:
		pos = (480, 250+height) #640, 360 for center of screen
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
	pygame.quit()
