import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.original1 = pygame.image.load('graphics/enemy/enemy1.png')
        self.original2 = pygame.image.load('graphics/enemy/enemy2.png')
        self.dead = pygame.image.load('graphics/enemy/enemy_dead.png')
        self.image = pygame.transform.flip(pygame.transform.scale(self.original1, (116,80)),True,False)
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.animationState = 0
        self.stopwatch = 0
        self.falling = 0
        self.getHit = False
    def enemy_animation(self):
        if self.animationState == 0:
            self.image = pygame.transform.flip(pygame.transform.scale(self.original2, (116,80)),True,False)
            self.animationState = 1
        elif self.animationState == 1:
            self.image = pygame.transform.flip(pygame.transform.scale(self.original1, (116,80)),True,False)
            self.animationState = 0
        elif self.animationState == 2:
            self.image = pygame.transform.flip(pygame.transform.scale(self.dead, (116,80)),True,False)
    def update(self):
        self.enemy_animation()
        self.rect.x -= 10
        if self.getHit:
            self.animationState = 2
            self.rect.y += self.falling
            self.falling += 0.5