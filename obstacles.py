import pygame
from random import randint

class GroundObstacles(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__() 
        if type == "tree":
            surf1 = pygame.Surface((150, 400))
            surf1.fill("Black")
            self.image =  surf1
            self.rect = self.image.get_rect(bottomleft = (1300, 780))
            #tree = pygame.image.load("graphics/PNG/tree03.png").convert_alpha()
            #self.image = tree
            #self.image = pygame.transform.scale(self.image, (204, 439))
            #self.rect = self.image.get_rect(bottomleft = (1300, 780))
        elif type == "grey house":
            surf2 = pygame.Surface((100, 450))
            surf2.fill("Red")
            self.image =  surf2
            self.rect = self.image.get_rect(bottomleft = (1400, 780))
            #house = pygame.image.load("graphics/PNG/house_grey_front.png").convert_alpha()
            #self.image = house
            #self.image = pygame.transform.scale(self.image, (204, 348))
            #self.rect = self.image.get_rect(bottomleft = (1400, 780))

    def move_obj(self):
        self.rect.x -= 3

    def update(self):
        self.move_obj()
        self.destroy()

    def destroy(self):
        if self.rect.x <= -200:
            self.kill()


class AirObstacles(pygame.sprite.Sprite):
    def __init__():
        super().__init__()
        
        