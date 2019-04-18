import pygame
from directions import Directions
from assets import head_img,bend_img,body_img,tail_img
pygame.init()
class Snake_tail(pygame.sprite.Sprite):
    '''Create a snake segment with Tail'''
    def __init__(self, x, y,direction):
        super().__init__()
        if direction == Directions.RIGHT:
            turn = -90
        elif direction == Directions.LEFT:
            turn = 90
        elif direction == Directions.DOWN:
            turn = 180
        else :
            turn = 0
        self.image = pygame.transform.rotate(tail_img,turn) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y    
 
class Snake_body(pygame.sprite.Sprite):
    ''' Creates a snake segment as body '''
    def __init__(self, x, y,direction):
        super().__init__() 
        if direction == Directions.UP:
            turn = -90
        elif direction == Directions.DOWN:
            turn = 90
        elif direction == Directions.LEFT:
            turn = 180
        else :
            turn = 0    
        self.image = pygame.transform.rotate(body_img,turn) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def is_bend(self):
        ''' used to differentiate between bend segments and straight segments '''
        return False
class Snake_bend(pygame.sprite.Sprite):
    '''creates a snake segment with bend'''
    def __init__(self, x, y,direction,old_direction):
        super().__init__() 
        if direction == Directions.UP:
            if old_direction == Directions.RIGHT:
                turn = -90
            if old_direction == Directions.LEFT:
                turn = -180
        elif direction == Directions.DOWN:
            if old_direction == Directions.RIGHT:
                turn = 0
            if old_direction == Directions.LEFT:
                turn = 90
        elif direction == Directions.LEFT:
            if old_direction == Directions.UP:
                turn = 0
            if old_direction == Directions.DOWN:
                turn = -90
        elif direction == Directions.RIGHT:
            if old_direction == Directions.UP:
                turn = 90
            if old_direction == Directions.DOWN:
                turn = 180
        else :
            turn = 0
        self.image = pygame.transform.rotate(bend_img,turn) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def is_bend(self):
        ''' used to differentiate between bend segments and straight segments '''
        return True

class Snake_head(pygame.sprite.Sprite):
    '''Creates a snake segment as snake head'''
    def __init__(self, x, y,direction):
        super().__init__()
        if direction == Directions.RIGHT:
            turn = -90
        elif direction == Directions.LEFT:
            turn = 90
        elif direction == Directions.DOWN:
            turn = 180
        else :
            turn = 0    
        self.image = pygame.transform.rotate(head_img,turn)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
