# НАСТРОЙКИ
import pygame

from config import BLACK, WHITE, ORANGE_1, ComicSansMS30, ShentoxRegular30


def detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK):
    WINDOW_WIDTH = WINDOW_WIDTH / 100 * 30
    pygame.draw.rect(WINDOW, ORANGE_1, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
    descent_y = draw_fps(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y)
    # descent_y = some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y) # МАКСИМУМ


def draw_fps(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK):
    Text = ShentoxRegular30.render(f'FPS: {int(CLOCK.get_fps())}', True, (0, 0, 0))

    w, h = Text.get_width(), Text.get_height()  # узнаем размер текста
    centre_x = WINDOW_WIDTH / 2 - w / 2
    descent_y = WINDOW_HEIGHT / 100 * 2

    WINDOW.blit(Text, (centre_x, descent_y))
    descent_y += WINDOW_HEIGHT / 100 + h
    return descent_y

def some_text(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, descent_y):
    CLOCK = pygame.time.Clock()
    Text = ShentoxRegular30.render(f'FPS: {CLOCK.get_fps()}', True, (0, 0, 0))

    w, h = Text.get_width(), Text.get_height()  # узнаем размер текста
    centre_x = WINDOW_WIDTH / 2 - w / 2

    WINDOW.blit(Text, (centre_x, descent_y))
    descent_y += WINDOW_HEIGHT / 100 + h
    return descent_y
