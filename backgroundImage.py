import pygame
from pygame.locals import *

class BackgroundImage:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.pic = pygame.image.load("graphics/junkyard.png")
        self.screen.blit(pygame.transform.scale(self.pic, (width, height)), (0, 0))
        
    def createBackground(self):
        barrel = pygame.image.load("assets/modernexteriors-win/Modern_Exteriors_32x32/ME_Theme_Sorter_32x32/3_City_Props_Singles_32x32/ME_Singles_City_Props_32x32_Barrel_3.png")
        self.screen.blit(barrel, ((20, 190)))
   
