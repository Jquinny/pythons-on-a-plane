# FIXME: Fancy Header Here Later

import pygame
from sys import exit
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original1 = pygame.image.load('graphics/plane/Fly (1).png').convert_alpha()
        self.original2 = pygame.image.load('graphics/plane/Fly (2).png').convert_alpha()
        self.shoot1 = pygame.image.load('graphics/plane/Shoot (1).png').convert_alpha()
        self.shoot2 = pygame.image.load('graphics/plane/Shoot (2).png').convert_alpha()
        self.shoot3 = pygame.image.load('graphics/plane/Shoot (3).png').convert_alpha()
        self.shoot4 = pygame.image.load('graphics/plane/Shoot (4).png').convert_alpha()
        self.shoot5 = pygame.image.load('graphics/plane/Shoot (5).png').convert_alpha()
        self.animationState = 0
        self.image = pygame.transform.scale(self.original1, (232,159))
        self.rect = self.image.get_rect()
    def create_rocket(self):
        return Rocket(self.rect.x,self.rect.y)
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
class Rocket(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load('graphics/bullet/shell.gif').convert_alpha()
        self.rect = self.image.get_rect(center = (pos_x+180,pos_y+118))
    def update(self):
        self.rect.x += 5
        if self.rect.x >= 1400:
            self.kill()
        

pygame.init()
pygame.display.set_caption('Pythons on a Plane')
# Create vars for screen size and width/height of screen
size = 1280,720
width, height = size
#background
background = pygame.image.load('graphics/backgrounds/colored_castle.png')
# Initialize pygame and set a screen variable
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#player
player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

#rocket 
rocket_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            rocket_group.add(player.create_rocket())
    screen.blit(background,(0,0))
            
    player_group.draw(screen)
    player_group.update()
    rocket_group.draw(screen)
    rocket_group.update()
    #rockets()
    pygame.display.update()
    clock.tick(60)

