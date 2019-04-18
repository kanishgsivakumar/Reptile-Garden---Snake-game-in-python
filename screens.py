import pygame
from constants import WIN_HEIGHT,WIN_WIDTH,WHITE,GRAY,BLACK,SILVER
from assets import font,bg,logo

def game_over(screen,score):
    '''
    displays game over screen
    '''
    gray_overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    gray_overlay.fill(GRAY)
    gray_overlay.set_colorkey(GRAY)
    pygame.draw.rect(gray_overlay,BLACK, [0, 0, WIN_WIDTH, WIN_HEIGHT])
    gray_overlay.set_alpha(99)
    screen.blit(gray_overlay, (0, 0))
    game_over = font.render(' Game over', True, WHITE)
    screen.blit(game_over, (WIN_WIDTH / 2 - game_over.get_width()/2, WIN_HEIGHT / 2 - 100))
    scoreline = font.render(
        'Score - {}'.format(score), True, WHITE)
    screen.blit(scoreline,(WIN_WIDTH/2 - scoreline.get_width()/2,WIN_HEIGHT/2 + scoreline.get_height(),))
    pygame.display.update()
    pygame.time.delay(2000)

def game_paused(screen,score):
    '''displays game over screen'''
    gray_overlay = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))
    gray_overlay.fill(GRAY)
    gray_overlay.set_colorkey(GRAY)
    pygame.draw.rect(gray_overlay,BLACK,[0,0,WIN_WIDTH,WIN_HEIGHT])
    gray_overlay.set_alpha(99)
    screen.blit(gray_overlay,(0,0))
    game_paused =font.render(" Game Paused",True,WHITE)
    w,h = game_paused.get_size()
    screen.blit(game_paused,(WIN_WIDTH/2-w/2,WIN_HEIGHT/2-h/2))
    scoreline = font.render(
        ' score - {}'.format(score), True, WHITE)
    screen.blit(scoreline, (WIN_WIDTH / 2 - scoreline.get_width()/2, WIN_HEIGHT / 2 + scoreline.get_height()))
    pygame.display.update()

def welcome(screen):
    welcome_screen = True
    screen.blit(bg,(0,0))
    screen.blit(logo,(WIN_WIDTH/2 - logo.get_width()/2,WIN_HEIGHT/2 - logo.get_height()/2))
    pygame.display.flip()
    while welcome_screen:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                welcome_screen = False
                done = True
        else:
            pygame.event.pump()
            if keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER]:
                welcome_screen = False

