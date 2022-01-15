# FIXME: Fancy Header Here Later

import pygame
from pygame.locals import *

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
