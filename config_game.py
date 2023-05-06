# Не трогать. Это автоматические параметры для игра.
import config

units = [] # юниты
units_coordinates = [] # их коорды
units_for_food = [] # коорды еды к которому идут юниты
units_for_duplicate = [] # сколько они сожрали
units_life = []  # сколько они прожили
unit_genes = [] # [налево, направо, наверх, вниз,            скорость, радиус, размножение, увеличение жизни]

# SPEED_UNIT_1 = config.SIZE_UNIT

food = []
start = False

now_year = 1
now_mouth = 1
time_step = 0
