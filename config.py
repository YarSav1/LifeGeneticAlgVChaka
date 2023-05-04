import pygame

# Просто текст экранов.
TEST = True

# Настройка экрана
SettingsWidth = 30  # Сколько будет занимать места боковая панель (в процентах)

# Настройка быстродействия
CLOCK_FPS = 120  # Сколько выполнять операций в секунду? FPS

# Настройки игры
SPAWN_FIRST_UNIT = 5  # Сколько заспавнится первых юнитов
SIZE_UNIT = 15  # в пикселях
RADIUS_UNIT = 300  # радиус у юнита в процентах от его размера

# цвета
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# Нестандартные цвета
ORANGE_1 = [242, 164, 89]
GREEN_1 = [25, 255, 25]

# Инициация шрифтов
pygame.font.init()
# Шрифты
ComicSansMS30 = pygame.font.SysFont('Comic Sans MS', 30)
ComicSansMS16 = pygame.font.SysFont('Comic Sans MS', 16)
ShentoxRegular30 = pygame.font.Font('Fonts/ShentoxRegular.ttf', 30)

# Чисто просто так
MAX_FPS = 0
FOR_MEDIUM_FPS = 0
FOR_MEDIUM_FPS_COUNT = 0
