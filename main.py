import pygame

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

CLOCK_FPS = 60  # Сколько выполнять операций в секунду? FPS

running = True
while running:
    CLOCK.tick(CLOCK_FPS)
    pygame.display.update()  # обновляем экран

    # Обрабатываем по разделам на экране.
    field_settings.detection_win.detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK)
    field_simulation.detection_win.detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
