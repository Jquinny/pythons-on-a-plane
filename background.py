import pygame
from random import randint

class Background(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__() 
        if type == "cloud1":
            cloud1_surf = pygame.image.load("graphics/PNG/cloud1.png") # might want to do .convert() when u have it all figured out
            self.image = cloud1_surf
            self.rect = self.image.get_rect(midbottom = (1400, randint(50, 600)))
        elif type == "cloud2":
            cloud5_surf = pygame.image.load("graphics/PNG/cloud5.png")
            self.image = cloud5_surf
            self.rect = self.image.get_rect(midbottom = (1400, randint(50, 600)))
        else:
            cloud9_surf = pygame.image.load("graphics/PNG/cloud9.png")
            self.image = cloud9_surf
            self.rect = self.image.get_rect(midbottom = (1400, randint(50, 600)))

    def move_clouds(self):
        self.rect.x -= 4

    def update(self):
        self.move_clouds()
        self.destroy()

    def destroy(self):
        if self.rect.x <= -200:
            self.kill()

