import pygame

# Просто текст экранов.
TEST = False

# Настройка экрана
SettingsWidth = 20  # Сколько будет занимать места боковая панель (в процентах) Ниже 15 уже наблюдаются несостыковки

# Настройка быстродействия
CLOCK_FPS = 30  # Сколько выполнять операций в секунду? FPS

# Настройки игры
DRAW_RADIUS = False  # Включить прорисовку радиуса | Слабо влияет на FPS


SPAWN_FIRST_UNIT = 20  # Сколько заспавнится первых юнитов
SIZE_UNIT = 10  # размер юнитов в пикселях
# RADIUS_UNIT = 6  # радиус у юнита во сколько раз от его размера
LEN_LIFE = 24 # Продолжительность жизни юнита в месяцах

ONE_YEAR = 150 # число обработок равному 1 игровому году.

ENERGY_FOOD = 1  # сколько энергии будет давать 1 еда
SIZE_FOOD = 5
SPAWN_START_FOOD = 10000  # сколько еды генерировать в начале
SPAWN_FOOD = 500  # сколько еды генерировать каждый раз

FOOD_FOR_PLUS_LIFE = 120 # сколько нужно еды, чтобы продлить себе жизнь<=================\/
PLUS_LIFE_AFTER = 24 # сколько МЕСЯЦЕВ жизни будет давать еда при использовании умения ВЫШЕ

FOOD_FOR_DUPLICATE = 100  # сколько нужно съесть еды(в энергии) чтобы размножиться
CHANCE_MUTATION = 5  # вероятность мутации в процентах. МАКСИМУМ 100

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

