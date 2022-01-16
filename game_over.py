#LEADERBOARD MENU, COMPATIBILE WITH FIREBASE

import game_database
import pygame
from pygame.locals import *

def game_over_screen(screen, score):
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(545, 440, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    background = pygame.image.load("graphics/BG.png")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text != '':
                            game_database.addScore(text, score)
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
        screen.blit(background, (0, 0))
        add_text(screen)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        #add_text(screen)
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        

def add_text(screen):
    pos = (390, 220)
    font = pygame.font.Font("graphics/bubble.ttf", 96)
    font_img = font.render('GAME OVER', True, (255, 255, 255))
    rect = font_img.get_rect(topleft=pos)
    screen.blit(font_img, rect)

    pos = (500, 400)
    font = pygame.font.Font(None, 32)
    font_img = font.render('Enter your username below', True, (255, 255, 255))
    rect = font_img.get_rect(topleft=pos)
    screen.blit(font_img, rect)


    

    


