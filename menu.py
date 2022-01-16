# FIXME: Fancy Header Here Later

import pygame
from sys import exit
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original1 = pygame.image.load('graphics/plane/Fly (1).png')
        self.original2 = pygame.image.load('graphics/plane/Fly (2).png')
        self.animationState = 0
        self.image = pygame.transform.scale(self.original1, (232,159))
        self.rect = self.image.get_rect()
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
        

        
    def update(self):
        self.player_input()
        self.player_animation()
            
colour_inactive = pygame.Color('lightskyblue3')
colour_active = pygame.Color('dodgerblue2')
text_font = pygame.font.Font(None, 32)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = colour_inactive
        self.text = text
        self.txt_surface = text_font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = colour_active if self.active else colour_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = text_font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

pygame.init()
pygame.display.set_caption('Pythons on a Plane')
# Create vars for screen size and width/height of screen
size = 1280,720
width, height = size

# Initialize pygame and set a screen variable
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#player
player = pygame.sprite.GroupSingle()
player.add(Player())

input_box1 = InputBox(100, 100, 140, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    player.draw(screen)
    player.update()
    pygame.display.update()
    clock.tick(60)