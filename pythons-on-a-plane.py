# FIXME: Fancy Header Here Later

import pygame
from sys import exit
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original1 = pygame.image.load('graphics/plane/Fly (1).png')
        self.original2 = pygame.image.load('graphics/plane/Fly (2).png')
        self.shoot1 = pygame.image.load('graphics/plane/Shoot (1).png')
        self.shoot2 = pygame.image.load('graphics/plane/Shoot (2).png')
        self.shoot3 = pygame.image.load('graphics/plane/Shoot (3).png')
        self.shoot4 = pygame.image.load('graphics/plane/Shoot (4).png')
        self.shoot5 = pygame.image.load('graphics/plane/Shoot (5).png')
        self.animationState = 0
        self.image = pygame.transform.scale(self.original1, (232,159))
        self.rect = self.image.get_rect()
    def player_shoot(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.animationState = 2
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x += -10
        if keys[pygame.K_w]:
            self.rect.y += -10
        if keys[pygame.K_s]:
            self.rect.y += 10
        if keys[pygame.K_d]:
            self.rect.x += 10
    def player_animation(self):
        if self.animationState == 0:
            self.image = pygame.transform.scale(self.original2, (232,159))
            self.animationState = 1
        elif self.animationState == 1:
            self.image = pygame.transform.scale(self.original1, (232,159))
            self.animationState = 0
        elif self.animationState == 2:
            self.image = pygame.transform.scale(self.shoot1, (232,159))
            self.animationState = 3
        elif self.animationState == 3:
            self.image = pygame.transform.scale(self.shoot2, (232,159))
            self.animationState = 4
        elif self.animationState == 4:
            self.image = pygame.transform.scale(self.shoot3, (232,159))
            self.animationState = 5
        elif self.animationState == 5:
            self.image = pygame.transform.scale(self.shoot4, (232,159))
            self.animationState = 6
        elif self.animationState == 6:
            self.image = pygame.transform.scale(self.shoot5, (232,159))
            self.animationState = 0
    def update(self):
        self.player_shoot()
        self.player_input()
        self.player_animation()
            

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
    player.update()
    pygame.display.update()
    clock.tick(5)

