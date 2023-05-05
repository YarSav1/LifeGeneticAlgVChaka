import pygame

# Просто текст экранов.
TEST = False

# Настройка экрана
SettingsWidth = 40  # Сколько будет занимать места боковая панель (в процентах) Ниже 15 уже наблюдаются несостыковки

# Настройка быстродействия
CLOCK_FPS = 60  # Сколько выполнять операций в секунду? FPS

# Настройки игры
DRAW_RADIUS = False  # Включить прорисовку радиуса | Слабо влияет на FPS

SPAWN_FIRST_UNIT = 100  # Сколько заспавнится первых юнитов
SIZE_UNIT = 3  # размер юнитов в пикселях
RADIUS_UNIT = 20  # радиус у юнита во сколько раз от его размера

ENERGY_FOOD = 10  # сколько энергии будет давать 1 еда
SIZE_FOOD = SIZE_UNIT / 5  # размер еды в пикселях
if SIZE_FOOD < 1:
    SIZE_FOOD = 1
SPAWN_START_FOOD = 300  # сколько еды генерировать в начале
SPAWN_FOOD_TIME = 5  # раз в сколько СЕКУНД будет спавниться еда
SPAWN_FOOD = 300  # сколько еды генерировать каждый раз

FOOD_FOR_DUPLICATE = 60  # сколько нужно съесть еды(в энергии) чтобы размножиться
CHANCE_MUTATION = 25  # вероятность мутации в процентах. МАКСИМУМ 100

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
