import pygame
from random import randint

class GroundObstacles(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__() 
        if type == "castle grey":
            castle = pygame.image.load("graphics/PNG/castle_grey.png").convert_alpha()
            self.image = castle
            self.image = pygame.transform.scale(self.image, (408, 364))
            self.rect = self.image.get_rect(midtop = (1400, randint(400, 550)))
        elif type == "tower grey":
            tower = pygame.image.load("graphics/PNG/tower_grey.png").convert_alpha()
            self.image = tower
            self.image = pygame.transform.scale(self.image, (132, 454))
            self.rect = self.image.get_rect(midtop = (1400, randint(250, 550)))

    def move_obj(self):
        self.rect.x -= 3

    def update(self):
        self.move_obj()
        self.destroy()

    def destroy(self):
        if self.rect.x <= -200:
            self.kill()


class AirObstacles(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        pass # need stuff here