
import pygame
from pygame.draw import *
from random import randint, random

from config import *


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

class Game:
    balls = {}
    angry_balls = {}
    score = 0
    id_counter = 0
    new_ball_timer = 0
    def __init__(self, screen, clock,spawn_time, font_style):
        self.screen = screen
        self.clock = clock
        self.spawn_time = spawn_time
        self.font_style = font_style

    def start(self):
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.is_click_on_ball(*event.pos)
            self.render_balls(self.clock.get_time())
            self.render_score()
            self.add_time(self.clock.get_time())
            pygame.display.update()
            self.screen.fill(BLACK)

    def render_balls(self, delta_time):
        for ball in self.balls.values():
            ball.x, ball.y = ball.x + ball.velocity_x*delta_time, ball.y + ball.velocity_y*delta_time
            ball.is_on_edge()
            circle(self.screen, ball.color, (ball.x, ball.y), ball.r)
        for ball in self.angry_balls.values():
            ball.x, ball.y = ball.x + ball.velocity_x*delta_time, ball.y + ball.velocity_y*delta_time
            ball.is_on_edge()
            draw_angry_man(self.screen, ball.x, ball.y, ball.r)

    def render_score(self):
        score_text = self.font_style.render(f'Score: {self.score}', False,(255, 255, 255))
        self.screen.blit(score_text,(10,50))

    def new_ball(self,class_id):
        if class_id == 0:
            self.balls[self.id_counter] =  Ball(randint(100,WIDTH - 100), randint(100,HEIGHT-100),random()-0.5,random()-0.5, randint(30,50),  COLORS[randint(0, 5)], self.id_counter, 1500)
        elif class_id == 1:
            self.angry_balls[self.id_counter] =  Angry_ball(randint(100,WIDTH - 100), randint(100,HEIGHT-100),(random()-0.5)*3,(random()-0.5)*3, randint(30,50),  COLORS[randint(0, 5)], self.id_counter, 1000)
        self.id_counter+=1

    def delete_ball(self,id, class_id):
        if class_id == 0:
            self.balls.pop(id)
        elif class_id == 1:
            self.angry_balls.pop(id)
    
    def add_time(self, delta_time):
        to_delete = []
        for ball in self.balls.values():
            ball.add_time(delta_time)
            if ball.timer >= ball.max_time:
                to_delete.append(ball.id)
        for ball in self.angry_balls.values():
            ball.add_time(delta_time)
            if ball.timer >= ball.max_time:
                ball.change_direction()
        for id in to_delete:
            self.delete_ball(id, 0)
        self.new_ball_timer+=delta_time
        if self.new_ball_timer >= self.spawn_time:
            self.new_ball_timer = 0
            if random() > 0.9:
                self.new_ball(1)
            else:
                self.new_ball(0)

    def is_click_on_ball(self, position_x, position_y):
        to_delete = []
        for ball in self.balls.values():
            if (position_x - ball.x)**2 + (position_y - ball.y)**2 <= ball.r**2:
                self.score+=1
                to_delete.append((ball.id, 0))
        for ball in self.angry_balls.values():
            if (position_x - ball.x)**2 + (position_y - ball.y)**2 <= ball.r**2:
                self.score+=5
                to_delete.append((ball.id,1))
        for id in to_delete:
            self.delete_ball(*id)
                    
class Ball:
    timer = 0

    def __init__(self, x, y,velocity_x, velocity_y, r, color, id, max_time):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.id = id
        self.max_time = max_time
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
    
    def is_on_edge(self):
        if (self.x + self.r>= WIDTH) or (self.x - self.r <= 0):
                self.velocity_x = -self.velocity_x
        if (self.y + self.r >= HEIGHT) or (self.y -self.r <= 0):
            self.velocity_y = -self.velocity_y

    def add_time(self,delta_time):
        self.timer += delta_time
    
class Angry_ball(Ball):
    timer = 0

    def change_direction(self):
        self.velocity_x += self.velocity_x*(random()-0.5)
        self.velocity_y += self.velocity_y*(random()-0.5)
        self.timer = 0


def init():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font_style = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    return (screen, font_style, clock)

screen, font_style, clock = init()
game = Game(screen, clock, 500, font_style)
game.start()
    

pygame.quit()