import pygame
from random import randint

class GroundObstacles(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "ground obj 1":
            surf1 = pygame.image.load("graphics/PNG/blue_pipe3.png")
            surf1_scaled = pygame.transform.scale(surf1, (150,300))
            if randint(0,1):
                self.image = surf1_scaled
                self.rect = self.image.get_rect(bottomleft = (1400, 780))
            else:
                surf1_flipped = pygame.transform.flip(surf1_scaled, True, True)
                self.image = surf1_flipped
                self.rect = self.image.get_rect(topleft = (1400, 0))

        elif type == "ground obj 2":
            surf2 = pygame.image.load("graphics/PNG/blue_pipe3.png")
            surf2_scaled = pygame.transform.scale(surf2, (125,350))
            if randint(0,1):
                self.image = surf2_scaled
                self.rect = self.image.get_rect(bottomleft = (1400, 780))
            else:
                surf2_flipped = pygame.transform.flip(surf2_scaled, True, True)
                self.image = surf2_flipped
                self.rect = self.image.get_rect(topleft = (1400, 0))
        
        elif type == "ground obj 3":
            surf3 = pygame.image.load("graphics/PNG/blue_pipe3.png")
            surf3_scaled = pygame.transform.scale(surf3, (100,400))
            if randint(0,1):
                self.image = surf3_scaled
                self.rect = self.image.get_rect(bottomleft = (1400, 780))
            else:
                surf3_flipped = pygame.transform.flip(surf3_scaled, True, True)
                self.image = surf3_flipped
                self.rect = self.image.get_rect(topleft = (1400, 0))

    def move_obj(self):
        self.rect.x -= 3

    def update(self):
        self.move_obj()
        self.destroy()

    def destroy(self):
        if self.rect.x <= -150:
            self.kill()


class AirObstacles(pygame.sprite.Sprite):
    def __init__(self, type, x, m):
        super().__init__()
        self.type = type
        self.slope = m
        self.x = x

        if type == "anvil":
            anvil_surf = pygame.image.load("graphics/PNG/question_block.png").convert()
            anvil_scaled = pygame.transform.scale(anvil_surf, (50, 50))
            self.image = anvil_scaled
            self.rect = self.image.get_rect(midbottom = (x,-100))

        else:
            asteroid_surf = pygame.image.load("graphics/PNG/asteroid4.png")
            asteroid_scaled = pygame.transform.scale(asteroid_surf, (75, 75))
            self.image = asteroid_scaled
            self.rect = self.image.get_rect(midbottom = (x,-100))
    
    def move_asteroid(self, slope):
        self.rect.x -= 4
        self.rect.y += slope
        self.slope += 0.005

    def move_anvil(self):
        self.rect.y += 2

    def update(self):
        if self.type == "asteroid":
            self.move_asteroid(self.slope)
            self.destroy()
        else:
            self.move_anvil()
            self.destroy()

    def destroy(self):
        if (self.rect.y >= 880) or (self.rect.x <= -75):
            self.kill()