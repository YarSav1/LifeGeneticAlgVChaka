# СИМУЛЯЦИЯ
import random

import pygame

import config
import config_game
from config import WHITE, SettingsWidth, TEST


def detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT):
    WINDOW_START = WINDOW_WIDTH / 100 * SettingsWidth
    WINDOW_WIDTH = WINDOW_WIDTH / 100 * (100-SettingsWidth) + WINDOW_START

    if TEST:
        some_draw(WINDOW,WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_START)
    else:
        pygame.draw.rect(WINDOW, WHITE, (WINDOW_START, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        _spawn(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)
        _draw_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)
        _draw_radius_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)

        _moving_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)

def some_draw(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    x = random.randint(WINDOW_START, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    pygame.draw.rect(WINDOW, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (x, y, 10, 10))

def _spawn(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    if len(config_game.units) != config.SPAWN_FIRST_UNIT:
        for unit in range(config.SPAWN_FIRST_UNIT):
            x = random.randint(WINDOW_START, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            color_unit = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            pygame.draw.rect(WINDOW, (color_unit),
                             (x, y, 10, 10))

            config_game.units[color_unit] = [x,y]
        print(config_game.units)

def _draw_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    for unit in config_game.units:
        x = config_game.units[unit][0]
        y = config_game.units[unit][1]
        color_unit = unit
        pygame.draw.rect(WINDOW, (color_unit),
                         (x, y, config.SIZE_UNIT, config.SIZE_UNIT))
def _draw_radius_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    for unit in config_game.units:
        x = config_game.units[unit][0]+config.SIZE_UNIT/2
        y = config_game.units[unit][1]+config.SIZE_UNIT/2
        color_unit = unit
        SIZE_RADIUS = config.SIZE_UNIT/100*config.RADIUS_UNIT
        pygame.draw.rect(WINDOW, (color_unit),
                         (x-SIZE_RADIUS/2, y-SIZE_RADIUS/2,
                          SIZE_RADIUS, SIZE_RADIUS),
                         1)

def _moving_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    for unit in config_game.units:
        config_game.units[unit][0]+=random.randint(-1, 1)
        config_game.units[unit][1]+=random.randint(-1, 1)