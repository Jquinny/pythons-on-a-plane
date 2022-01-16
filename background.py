import pygame
from random import randint

class Background(pygame.sprite.Sprite):
    def __init__(self, type, x_change):
        super().__init__()
        self.x_change = x_change

        if type == "cloud1":
            cloud1_surf = pygame.image.load("graphics/PNG/cloud1.png").convert_alpha()
            self.image = cloud1_surf
            self.image.set_alpha(150)
            self.rect = self.image.get_rect(midbottom = (1400, randint(50, 600)))
        elif type == "cloud5":
            cloud5_surf = pygame.image.load("graphics/PNG/cloud5.png").convert_alpha()
            self.image = cloud5_surf
            self.image.set_alpha(150)
            self.rect = self.image.get_rect(midbottom = (1400, randint(50, 600)))
        else:
            cloud9_surf = pygame.image.load("graphics/PNG/cloud9.png").convert_alpha()
            self.image = cloud9_surf
            self.image.set_alpha(150)
            self.rect = self.image.get_rect(midbottom = (1400, randint(50, 600)))

    def move_clouds(self):
        self.rect.x -= self.x_change

    def update(self):
        self.move_clouds()
        self.destroy()

    def destroy(self):
        if self.rect.x <= -200:
            self.kill()

