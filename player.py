import pygame
from rockets import Rocket
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
        self.dead = pygame.image.load('graphics/plane/Dead (1).png').convert_alpha()
        self.getHit = False
        self.animationState = 0
        self.image = pygame.transform.scale(self.original1, (116,80))
        self.rect = self.image.get_rect()
        self.rect.y = 360
        self.stopwatch = 0
    def create_rocket(self):
        return Rocket(self.rect.x,self.rect.y)
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > -100:
            self.rect.x += -10
        if keys[pygame.K_w] and self.rect.y > -50:
            self.rect.y += -10
        if keys[pygame.K_s] and self.rect.y < 700:
            self.rect.y += 10
        if keys[pygame.K_d] and self.rect.x < 1100:
            self.rect.x += 10
    def player_animation(self):
        if self.animationState == 0:
            self.image = pygame.transform.scale(self.original2, (116,80))
            self.animationState = 1
        elif self.animationState == 1:
            self.image = pygame.transform.scale(self.original1, (116,80))
            self.animationState = 0
        elif self.animationState == 2:
            self.image = pygame.transform.scale(self.shoot1, (116,80))
            self.animationState = 3
        elif self.animationState == 3:
            self.image = pygame.transform.scale(self.shoot2, (116,80))
            self.animationState = 4
        elif self.animationState == 4:
            self.image = pygame.transform.scale(self.shoot3, (116,80))
            self.animationState = 5
        elif self.animationState == 5:
            self.image = pygame.transform.scale(self.shoot4, (116,80))
            self.animationState = 6
        elif self.animationState == 6:
            self.image = pygame.transform.scale(self.shoot5, (116,80))
            self.animationState = 0
    def update(self):
        self.player_input()
        self.player_animation()