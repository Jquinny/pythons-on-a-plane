# FIXME: Fancy Header Here Later

import pygame
from sys import exit
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original = pygame.image.load('pythons-on-a-plane/graphics/plane/Fly_(1).png')
        self.image = pygame.transform.scale(self.original, (232,159))
        self.rect = self.image.get_rect()
    def player_input():
        keys = pygame.key.get_pressed()
        if keys

pygame.init()
pygame.display.set_caption('Pythons on a Plane')
# Create vars for screen size and width/height of screen
size = 1280,720
width, height = size

# Initialize pygame and set a screen variable
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#player
player = pygame.sprite.GroupSingle()
player.add(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    player.draw(screen)
    pygame.display.update()
    clock.tick(60)

