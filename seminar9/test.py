
import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
WIDTH = 1200
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.SysFont('serif', 48)



class Game:
    balls = {}
    score = 0
    id_counter = 0
    new_ball_timer = 0
    def __init__(self, screen, spawn_time):
        self.screen = screen
        self.spawn_time = spawn_time
    def new_ball(self):
        self.balls[self.id_counter] =  Ball(randint(100,WIDTH - 100), randint(100,HEIGHT-100),0,0, randint(30,50),  COLORS[randint(0, 5)], self.id_counter, 1500)
        self.id_counter+=1
    def delete_ball(self, id):
        self.balls.pop(id)
    
    def add_time(self, delta_time):
        to_delete = []
        for ball in self.balls.values():
            ball.add_time(delta_time)
            if ball.timer >= ball.max_time:
                to_delete.append(ball.id)
        for id in to_delete:
            self.delete_ball(id)
        self.new_ball_timer+=delta_time
        if self.new_ball_timer >= self.spawn_time:
            self.new_ball_timer = 0
            self.new_ball()


    def is_click_on_ball(self, position_x, position_y):
        to_delete = []
        for ball in self.balls.values():
            if (position_x - ball.x)**2 + (position_y - ball.y)**2 <= ball.r**2:
                self.score+=1
                to_delete.append(ball.id)
        for id in to_delete:
            self.delete_ball(id)
    
                
class Ball:
    timer = 0
    def __init__(self, x, y,velocityx, velocityy, r, color, id, max_time):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.id = id
        self.max_time = max_time
    
    def add_time(self,delta_time):
        self.timer += delta_time
    

def render_balls(game):
    for ball in game.balls.values():
        circle(game.screen, ball.color, (ball.x, ball.y), ball.r)



pygame.display.update()
clock = pygame.time.Clock()
finished = False
game = Game(screen, 200)
game.new_ball()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.is_click_on_ball(*event.pos)
    render_balls(game)
    score_text = f2.render(f'Score: {game.score}', False,
                  (0, 180, 0))
    screen.blit(score_text,(10,50))
    game.add_time(clock.get_time())
    pygame.display.update()
    screen.fill(BLACK)
    

pygame.quit()