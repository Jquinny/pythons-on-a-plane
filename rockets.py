import pygame
class Rocket(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load('graphics/bullet/shell.gif').convert_alpha()
        self.one = pygame.image.load('graphics/explosion/1.png').convert_alpha()
        self.two = pygame.image.load('graphics/explosion/2.gif').convert_alpha()
        self.three = pygame.image.load('graphics/explosion/3.gif').convert_alpha()
        self.four = pygame.image.load('graphics/explosion/4.gif').convert_alpha()
        self.five = pygame.image.load('graphics/explosion/5.gif').convert_alpha()
        self.six = pygame.image.load('graphics/explosion/6.gif').convert_alpha()
        self.seven = pygame.image.load('graphics/explosion/7.gif').convert_alpha()
        self.eight = pygame.image.load('graphics/explosion/8.gif').convert_alpha()
        self.nine = pygame.image.load('graphics/explosion/9.gif').convert_alpha()
        self.ten = pygame.image.load('graphics/explosion/10.gif').convert_alpha()
        self.eleven = pygame.image.load('graphics/explosion/11.gif').convert_alpha()
        self.twelve = pygame.image.load('graphics/explosion/12.gif').convert_alpha()
        self.thirteen = pygame.image.load('graphics/explosion/13.gif').convert_alpha()
        self.fourteen = pygame.image.load('graphics/explosion/14.gif').convert_alpha()
        self.fifteen = pygame.image.load('graphics/explosion/15.gif').convert_alpha()
        self.rect = self.image.get_rect(center = (pos_x+90,pos_y+59))
        self.speed = 0
        self.getHit = False
        self.animationState = -1
    def explosion(self):
        if self.animationState == -1:
            self.animationState = 0
        elif self.animationState == 0:
            self.rect.x -= 50
            self.rect.y -= 50
            self.image = self.one
            self.animationState = 1
        elif self.animationState == 1:
            self.image = self.two
            self.animationState = 2
        elif self.animationState == 2:
            self.image = self.three
            self.animationState = 3
        elif self.animationState == 3:
            self.image = self.four
            self.animationState = 4
        elif self.animationState == 4:
            self.image = self.five
            self.animationState = 5
        elif self.animationState == 5:
            self.image = self.six
            self.animationState = 6
        elif self.animationState == 6:
            self.image = self.seven
            self.animationState = 7
        elif self.animationState == 7:
            self.image = self.eight
            self.animationState = 8
        elif self.animationState == 8:
            self.image = self.nine
            self.animationState = 9
        elif self.animationState == 9:
            self.image = self.ten
            self.animationState = 10
        elif self.animationState == 10:
            self.image = self.eleven
            self.animationState = 11
        elif self.animationState == 11:
            self.image = self.twelve
            self.animationState = 12
        elif self.animationState == 12:
            self.image = self.thirteen
            self.animationState = 13
        elif self.animationState == 13:
            self.image = self.fourteen
            self.animationState = 14
        elif self.animationState == 14:
            self.image = self.fifteen
            self.kill()
    def update(self):
        if self.getHit:
            self.explosion()
        else:
            self.speed += 0.4
            self.rect.x += self.speed
            if self.rect.x >= 1400:
                self.kill()