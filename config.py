import pygame

# Просто текст экранов.
TEST = False

# Настройка экрана
SettingsWidth = 30  # Сколько будет занимать места боковая панель (в процентах)

# Настройка быстродействия
CLOCK_FPS = 1000  # Сколько выполнять операций в секунду? FPS

# Настройки игры
DRAW_RADIUS = True # Включить прорисовку радиуса

SPAWN_FIRST_UNIT = 20  # Сколько заспавнится первых юнитов
SIZE_UNIT = 20  # размер юнитов в пикселях
RADIUS_UNIT = 5  # радиус у юнита во сколько раз от его размера

SIZE_FOOD = SIZE_UNIT/5 # размер еды в пикселях
SPAWN_START_FOOD = 500  # сколько еды генерировать в начале
SPAWN_FOOD_TIME = 5  # раз в сколько СЕКУНД будет спавниться еда
SPAWN_FOOD = 200  # сколько еды генерировать каждый раз

# цвета
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# Нестандартные цвета
ORANGE_1 = [242, 164, 89]
GREEN_1 = [25, 255, 25]
RED_1 = [193, 0, 32]

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
