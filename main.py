from enum import Enum
import pygame
from directions import Directions
from  Snake import Snake_bend,Snake_body,Snake_head,Snake_tail 
from assets import bg,logo,font,font_s
from constants import *
from screens import *
from apple import *
# Globals
is_apple = False
allspriteslist = pygame.sprite.Group()
is_turned = False 
done = False
Pause = False
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([WIN_WIDTH,WIN_HEIGHT])
pygame.display.set_caption('Reptile Gardens')
# welcome screen
welcome(screen)
x_change = segment_width + segment_margin
y_change = 0
score = 0
direction,old_direction = Directions.RIGHT,Directions.RIGHT
dir_list=[Directions.RIGHT,]

# creates snake
snake_segments = []
for i in range(7):
    x = WIN_WIDTH/2 - (segment_width + segment_margin) * i
    y = WIN_HEIGHT/2
    if i == 0:
        segment = Snake_head(x, y,direction)
    elif i == 6:
        segment = Snake_tail(x,y,direction)
    else:
        segment = Snake_body(x, y,direction)
    snake_segments.append(segment)
    allspriteslist.add(segment)
while not done:
    if not Pause:
        speed = speed*1.001
        head = snake_segments[0]
        tail = snake_segments[-1]
# Checks for key presses 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F7:
                    Pause = True
                    continue
                if event.key == pygame.K_LEFT:
                    if direction not in (Directions.RIGHT , Directions.LEFT ):
                        is_turned =True
                        x_change = (segment_width + segment_margin) * -1
                        y_change = 0
                        old_direction,direction = direction,Directions.LEFT
                        dir_list.append(direction)
                if event.key == pygame.K_RIGHT:
                    if direction not in (Directions.LEFT, Directions.RIGHT ):
                        is_turned =True
                        x_change = (segment_width + segment_margin)
                        y_change = 0
                        old_direction,direction = direction, Directions.RIGHT
                        dir_list.append(direction)
                if event.key == pygame.K_UP:
                    if direction not in ( Directions.DOWN , Directions.UP ):
                        is_turned =True
                        x_change = 0
                        y_change = (segment_height + segment_margin) * -1
                        old_direction,direction = direction,Directions.UP
                        dir_list.append(direction)
                if event.key == pygame.K_DOWN:
                    if direction not in (Directions.UP , Directions.DOWN):
                        is_turned =True 
                        x_change = 0
                        y_change = (segment_height + segment_margin)
                        old_direction,direction = direction,Directions.DOWN
                        dir_list.append(direction)
# checks for wheater apple is available if not it adds the apple to screen
        if not(is_apple):
            apple = Apple()
            allspriteslist.add(apple)
            is_apple = True
# checks if apple and snake head colides 
        if head.rect.colliderect(apple):
            score += 1 
            old_segment = apple
            is_apple = False
        else:
            if snake_segments[-2].is_bend():
                dir_list.pop(0)
            new_tail = Snake_tail(snake_segments[-2].rect.x,snake_segments[-2].rect.y,dir_list[0])
            old_tail = snake_segments.pop()
            old_segment = snake_segments.pop()
            snake_segments.append(new_tail)
        allspriteslist.remove(old_segment)
        allspriteslist.remove(old_tail)
        allspriteslist.add(new_tail)
# checks if  snake heats his tail 
        collide_segments= (head.rect.collidelistall(snake_segments[1:]))
        for i in collide_segments:
            if not(i  in (-1,0)):
                done = True
        x = snake_segments[0].rect.x + x_change
        y = snake_segments[0].rect.y + y_change
# checks wheather the snake has left the game boundaries
        if(x<68)or(x>720):
            done = True
        if(y<52)or(y>586):
            done = True
        segment1 = Snake_head(x, y,direction)
        if is_turned:
            segment2 = Snake_bend(head.rect.x,head.rect.y,direction,old_direction)
            is_turned = False
        else:            
            segment2 = Snake_body(head.rect.x,head.rect.y,direction)
# Insert new segment into the list
        snake_segments.insert(0, segment1)
        old_segment = snake_segments.pop(1)
        snake_segments.insert(1,segment2)
        allspriteslist.add(segment1)
        allspriteslist.add(segment2)
        allspriteslist.remove(old_segment)
# Clear screen
        screen.fill(BLACK)
        screen.blit(bg,(0,0))
        score_line1 = font_s.render("score",True,WHITE)
        screen.blit(score_line1,(25,15))
        score_line2 = font_s.render("{}".format(score),True,WHITE)
        screen.blit(score_line2,(25,35))
# -- Draw everything
        allspriteslist.draw(screen)    
# Flip screen
        pygame.display.flip()
# Pause
        clock.tick(abs(speed))
    else:
# Game paused
        game_paused(screen,score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_F8:
                    Pause = False
# Game over
game_over(screen,score)
pygame.quit()