from textwrap import fill
import pygame
from pygame.draw import *
YELLOW = (225, 225, 0)
BLACK = (0,0,0)
RED = (255,0,0)
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
color = (255, 255, 255)
screen.fill((255,255,255))
circle(screen, YELLOW, (200, 200), 100)
rect(screen, BLACK, (150, 240,100,15) )
circle(screen, RED, (160, 160), 25)
circle(screen, BLACK, (160, 160), 25, 1)
circle(screen, BLACK, (160, 160), 10)
polygon(screen, BLACK, [(190, 145), (135,125), (140, 120), (190, 140)])
circle(screen, RED, (240, 160), 20)
circle(screen, BLACK, (240, 160), 20, 1)
circle(screen, BLACK, (240, 160), 10)
polygon(screen, BLACK, [(220, 145), (260,130), (260, 125), (220, 140)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()