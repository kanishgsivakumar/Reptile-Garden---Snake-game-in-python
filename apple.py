import pygame
import  random as rdm
from constants import segment_height,segment_margin,segment_width
from assets import apple_img
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x = rdm.randrange(start=68,stop = 730,step=(segment_width+segment_margin))
        y = rdm.randrange(start=52,stop = 580,step=(segment_height+segment_margin))
        self.image = apple_img        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y