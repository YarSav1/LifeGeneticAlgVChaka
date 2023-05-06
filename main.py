import threading

import pygame

import config
import config_game
import field_settings.detection_win
import field_simulation.detection_win

# Инициация модулей pygame
pygame.init()

infoObject = pygame.display.Info()  # Информация о размерах экрана.
# Определяем размер экрана.
WINDOW_WIDTH = infoObject.current_w
WINDOW_HEIGHT = infoObject.current_w // 100 * 55

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # инициализация окна
WINDOW.set_alpha(None)
CLOCK = pygame.time.Clock()

if config.TEST:
    print('Включен режим теста. Выключите его, чтобы смотреть ща симуляцией.')
running = 1
while running == 1:
    CLOCK.tick(config.CLOCK_FPS)
    # if config.FOR_MEDIUM_FPS_COUNT >=10:
    #     config.FOR_MEDIUM_FPS_COUNT = 0
    config.FOR_MEDIUM_FPS_COUNT += 1

    pygame.display.update()  # обновляем экран

    # Обрабатываем по разделам на экране.
    threading.Thread(target=field_settings.detection_win.detection, args=(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK)).start()
    field_simulation.detection_win.detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT)

    config_game.time_step+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = 0

# a = random.choices([5, 7], weights=[1000000000, 10], k=1)

