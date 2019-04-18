import pygame
import os
pygame.init()
# image assets

bg = pygame.image.load(os.path.join("res","snake_bg.png"))
logo = pygame.image.load(os.path.join("res","logo.png"))
apple_img = pygame.image.load(os.path.join("res","apple.png"))
head_img = pygame.image.load(os.path.join("res","snake_head.png"))
bend_img = pygame.image.load(os.path.join("res","snake_bend.png"))
body_img = pygame.image.load(os.path.join("res","snake_body.png"))
tail_img = pygame.image.load(os.path.join("res","snake_tail.png"))
# font assets
title = pygame.font.Font("barcade.ttf",60)
font = pygame.font.Font("emulogic.ttf",50)
font_s = pygame.font.Font("emulogic.ttf",10)