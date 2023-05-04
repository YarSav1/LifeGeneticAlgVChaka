# СИМУЛЯЦИЯ
import random

import pygame

from config import WHITE


def detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT):
    WINDOW_START = WINDOW_WIDTH / 100 * 30
    WINDOW_WIDTH = WINDOW_WIDTH / 100 * 70 + WINDOW_START
    some_draw(WINDOW,WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_START)

    # pygame.draw.rect(WINDOW, WHITE, (WINDOW_START, 0, WINDOW_WIDTH, WINDOW_HEIGHT))

def some_draw(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    x = random.randint(WINDOW_START, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    pygame.draw.rect(WINDOW, WHITE, (x, y, 1, 1))


