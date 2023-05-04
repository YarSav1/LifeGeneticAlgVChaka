# НАСТРОЙКИ
import pygame

import config
from config import BLACK, WHITE, ORANGE_1, ComicSansMS30, ShentoxRegular30


def detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK):
    WINDOW_WIDTH = WINDOW_WIDTH / 100 * config.SettingsWidth
    pygame.draw.rect(WINDOW, ORANGE_1, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
    descent_y = draw_fps(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK)
    descent_y = max_fps(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    descent_y = medium_fps(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    descent_y = line(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    if config.TEST:
        this_test(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    else:
        pass


def draw_fps(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK):
    FPS = int(CLOCK.get_fps())
    Text = ShentoxRegular30.render(f'FPS: {FPS}', True, (0, 0, 0))
    if config.MAX_FPS < FPS:
        config.MAX_FPS = FPS
    config.FOR_MEDIUM_FPS += FPS

    w, h = Text.get_width(), Text.get_height()  # узнаем размер текста
    centre_x = WINDOW_WIDTH / 2 - w / 2
    descent_y = WINDOW_HEIGHT / 100 * 2

    WINDOW.blit(Text, (centre_x, descent_y))
    descent_y += WINDOW_HEIGHT / 100 + h

    return descent_y


def max_fps(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y):
    Text = ShentoxRegular30.render(f'MaxFPS: {config.MAX_FPS}', True, (0, 0, 0))

    w, h = Text.get_width(), Text.get_height()  # узнаем размер текста
    centre_x = WINDOW_WIDTH / 2 - w / 2

    WINDOW.blit(Text, (centre_x, descent_y))
    descent_y += WINDOW_HEIGHT / 100 + h
    return descent_y


def medium_fps(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y):
    MD_FPS = int(config.FOR_MEDIUM_FPS / config.FOR_MEDIUM_FPS_COUNT)
    Text = ShentoxRegular30.render(f'MediumFPS: {MD_FPS}', True, (0, 0, 0))

    w, h = Text.get_width(), Text.get_height()  # узнаем размер текста
    centre_x = WINDOW_WIDTH / 2 - w / 2

    WINDOW.blit(Text, (centre_x, descent_y))
    descent_y += WINDOW_HEIGHT / 100 + h
    return descent_y


def line(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y):
    h = WINDOW_HEIGHT / 100
    pygame.draw.rect(WINDOW, BLACK, (0, descent_y, WINDOW_WIDTH, h))
    descent_y += WINDOW_HEIGHT / 100 + h
    return descent_y


def this_test(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y):
    Text = ShentoxRegular30.render(f'Включен тестовый режим.', True, (0, 0, 0))

    w, h = Text.get_width(), Text.get_height()  # узнаем размер текста
    centre_x = WINDOW_WIDTH / 2 - w / 2

    WINDOW.blit(Text, (centre_x, descent_y))
    descent_y += WINDOW_HEIGHT / 100 + h
    return descent_y
