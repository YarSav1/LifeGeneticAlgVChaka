import pygame

import config
import field_settings.detection_win
import field_simulation.detection_win

# Инициация модулей pygame
pygame.init()

infoObject = pygame.display.Info()  # Информация о размерах экрана.
# Определяем размер экрана.
WINDOW_WIDTH = infoObject.current_w
WINDOW_HEIGHT = infoObject.current_w // 100 * 55

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # инициализация окна
CLOCK = pygame.time.Clock()

if config.TEST:
    print('Включен режим теста. Выключите его, чтобы смотреть ща симуляцией.')

running = True
while running:
    CLOCK.tick(config.CLOCK_FPS)
    # if config.FOR_MEDIUM_FPS_COUNT >=10:
    #     config.FOR_MEDIUM_FPS_COUNT = 0
    config.FOR_MEDIUM_FPS_COUNT += 1

    pygame.display.update()  # обновляем экран

    # Обрабатываем по разделам на экране.
    field_settings.detection_win.detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK)
    field_simulation.detection_win.detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
