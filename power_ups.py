import pygame

class PowerUps(pygame.sprite.Sprite):
    def __init__(self, type):
        """ will need an if statement to differentiate the type of power up
        will also need to have them move at the same rate as the pipes and clouds
        Notes for other things (just quality of life stuff):
        ** NOTE: also need to change cloud movement to be the same speed as pipes
        *** NOTE: also need to increase difficulty scaling in main file
        **** NOTE: convert the difficulty scaling if statements into a function for modularity (in main file). Maybe also put the drawing/updating into a function as well
        """
        pass