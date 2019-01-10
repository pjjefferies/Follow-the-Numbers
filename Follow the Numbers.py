# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:16:18 2019

@author: PaulJ
"""

from time import time
from random import randint
import pgzrun

WIDTH = 400
HEIGHT = 400
NO_DOTS = 10
TIME_DOT_MULTIPLIER = 2.0
TIME_LIMIT = NO_DOTS * TIME_DOT_MULTIPLIER
dots = []
lines = []
next_dot = 0
start_time = time()

# score = 0
# game_over = False

def create_dots():
    for dot in range(0, NO_DOTS):
        actor = Actor('dot')
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(actor)

# fox = Actor('fox')
# fox.pos = 100, 100

# coin = Actor('coin')
# coin.pos = 200, 200

def update():
    time_elapsed = time() - start_time
    time_remaining = TIME_LIMIT - time_elapsed
    if time_remaining <= 0:
        exit()

def draw():
    screen.fill('black')
    number = 1
    for dot in dots:
        screen.draw.text(str(number),
                         (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
    time_elapsed = time() - start_time
    time_remaining = int(TIME_LIMIT - time_elapsed)
    screen.draw.text('Time: ' + str(time_remaining),
                     color='white',
                     topright=(WIDTH-10, 10))

def on_mouse_down(pos):
    global next_dot
    global lines
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot -1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
        if next_dot >= NO_DOTS:
            next_level()
    else:
        lines = []
        next_dot = 0

def next_level():
    global NO_DOTS, lines, start_time, dots
    NO_DOTS += 2
    TIME_LIMIT = NO_DOTS * TIME_DOT_MULTIPLIER
    start_time = time()
    dots = []
    lines = []
    create_dots()

create_dots()

pgzrun.go()
