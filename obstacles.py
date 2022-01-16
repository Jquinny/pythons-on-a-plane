import pygame
from random import randint

class GroundObstacles(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "ground obj 1":
            surf1 = pygame.Surface((150, 350))
            surf1.fill("Black")
            self.image = surf1
            if randint(0,1):
                self.rect = self.image.get_rect(bottomleft = (1400, 780))
            else:
                self.rect = self.image.get_rect(topleft = (1400, 0))

        elif type == "ground obj 2":
            surf2 = pygame.Surface((100, 400))
            surf2.fill("Red")
            self.image = surf2
            if randint(0,1):
                self.rect = self.image.get_rect(bottomleft = (1400, 780))
            else:
                self.rect = self.image.get_rect(topleft = (1400, 0))
        
        elif type == "ground obj 3":
            surf3 = pygame.Surface((75, 450))
            surf3.fill("Green")
            self.image = surf3
            if randint(0,1):
                self.rect = self.image.get_rect(bottomleft = (1400, 780))
            else:
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
            anvil = pygame.Surface((50, 50))
            anvil.fill("Green")
            self.image = anvil
            self.rect = self.image.get_rect(midbottom = (x,-100))

        else:
            asteroid = pygame.Surface((50, 50))
            asteroid.fill("Blue")
            self.image = asteroid
            self.rect = self.image.get_rect(midbottom = (x,-100))
    
    def move_asteroid(self, x, slope):
        self.rect.x -= 2
        x_change = x - self.rect.x
        print(x_change)
        self.rect.y += slope*(x_change**2)
    
    def move_anvil(self):
        self.rect.y += 2

    def update(self):
        if self.type == "asteroid":
            self.move_asteroid(self.x, self.slope)
            self.destroy()
        else:
            self.move_anvil()
            self.destroy()

    def destroy(self):
        if (self.rect.y >= 880) or (self.rect.x <= -75):
            self.kill()