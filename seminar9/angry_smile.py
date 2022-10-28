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
def draw_angry_man(screen, x,y,r):
    circle(screen, YELLOW, (x, y), r)
    rect(screen, BLACK, (x-r/2, y+0.4*r,r,0.15*r) )
    circle(screen, RED, (x-0.4*r, y-0.4*r), r/4)
    circle(screen, BLACK, (x-0.4*r, y-0.4*r), r/4, 1)
    circle(screen, BLACK, (x-0.4*r, y-0.4*r), r/10)
    polygon(screen, BLACK, [(x-r/10, y - r*0.55), (x-r*0.65,y - r*0.75), (x-r*0.6, y-r*0.8), (x-r/10, y-0.6*r)])
    circle(screen, RED, (x+0.4*r, y-0.4*r), r/5)
    circle(screen, BLACK, (x+0.4*r, y-0.4*r), r/5, 1)
    circle(screen, BLACK, (x+0.4*r, y-0.4*r), r/10)
    polygon(screen, BLACK, [(x+0.2*r, y - 0.55*r), (x+0.6*r,y-0.7*r), (x+0.6*r, y-0.75*r), (x+0.2*r, y-0.6*r)])

draw_angry_man(screen, 200,200,100)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()