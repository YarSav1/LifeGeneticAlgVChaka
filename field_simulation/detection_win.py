# СИМУЛЯЦИЯ
import random
import time
from collections import Counter

import pygame

import config
import config_game
from config import WHITE, SettingsWidth, TEST


def detection(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT):
    WINDOW_START = WINDOW_WIDTH / 100 * SettingsWidth
    WINDOW_WIDTH = WINDOW_WIDTH / 100 * (100 - SettingsWidth) + WINDOW_START

    if TEST:
        some_draw(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)
    else:
        pygame.draw.rect(WINDOW, WHITE, (WINDOW_START, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        _spawn(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)
        _spawn_food(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)
        _spawn_food_every_time(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)

        _draw_food(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)

        if config_game.units:
            _draw_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)
            _draw_radius_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)
            _moving_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START)

        _zero_step()

        if config_game.units:
            _duplicate(WINDOW)
            _plus_life(WINDOW)
            _food_after_dead(WINDOW)


def some_draw(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    x = random.randint(WINDOW_START, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    pygame.draw.rect(WINDOW, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x, y, 10, 10))


# a = random.choices([5, 7], weights=[1000000000, 10], k=1)

def _insert_unit(id_unit, x, y, unit=None):
    config_game.units.append(id_unit)
    config_game.units_coordinates.append([x, y])
    config_game.units_for_food.append([None, None])
    config_game.units_for_duplicate.append(10)
    config_game.units_life.append(0)
    if unit is None:
        #  [налево, направо, наверх, вниз, скорость, радиус, размножение, увеличение жизни]
        left, right, up, down = random.randint(1, 100), random.randint(1, 100), \
                                random.randint(1, 100), random.randint(1, 100)
        speed, radius, duplicate, plus_life = random.randint(1, config.SIZE_UNIT), random.randint(1, 10), \
                                              random.randint(1, 100), random.randint(1, 100)
        stop = random.randint(1, 100)
        config_game.unit_genes.append([left, right, up, down, speed, radius, duplicate, plus_life, stop])
    else:
        if random.choices([True, False], weights=[config.CHANCE_MUTATION, 100 - config.CHANCE_MUTATION], k=1)[
            0] is False:
            config_game.unit_genes.append(config_game.unit_genes[config_game.units.index(unit)])
        else:
            genes = random.choice(config_game.unit_genes[config_game.units.index(unit)])
            index_genes = config_game.unit_genes[config_game.units.index(unit)].index(genes)
            if index_genes in [0, 1, 2, 3, 6, 7, 8]:
                new_gen = random.randint(1, 100)
            elif index_genes == 4:
                new_gen = random.randint(1, config.SIZE_UNIT)
            elif index_genes == 5:
                new_gen = random.randint(1, 10)
            else:
                return
            new_genes = []
            for gen_ in config_game.unit_genes[config_game.units.index(unit)]:
                if config_game.unit_genes[config_game.units.index(unit)].index(gen_) == index_genes:
                    gen_ = new_gen
                new_genes.append(gen_)
            config_game.unit_genes.append(new_genes)
    # print(config_game.unit_genes)


def _delete_unit(unit):
    index_unit = config_game.units.index(unit)
    config_game.units.remove(unit)
    config_game.units_coordinates.remove(config_game.units_coordinates[index_unit])
    config_game.units_for_food.remove(config_game.units_for_food[index_unit])
    config_game.units_for_duplicate.remove(config_game.units_for_duplicate[index_unit])
    config_game.units_life.remove(config_game.units_life[index_unit])
    config_game.unit_genes.remove(config_game.unit_genes[index_unit])


def _spawn(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    if config_game.start is False:
        for unit in range(config.SPAWN_FIRST_UNIT):
            x = random.randint(WINDOW_START, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            color_unit = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            pygame.draw.rect(WINDOW, (color_unit),
                             (x, y, config.SIZE_UNIT, config.SIZE_UNIT))
            _insert_unit(color_unit, x, y)

        print(config_game.units)
        print(config_game.units_coordinates)


def _spawn_food(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    if config_game.start is False:
        for food in range(config.SPAWN_START_FOOD):
            x = random.randint(WINDOW_START, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            color_food = config.RED_1
            pygame.draw.rect(WINDOW, (color_food),
                             (x, y, config.SIZE_FOOD, config.SIZE_FOOD))

            config_game.food.append([x, y])
        config_game.start = True


def _draw_food(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    for food in config_game.food:
        x = food[0]
        y = food[1]
        color_food = config.RED_1
        pygame.draw.rect(WINDOW, (color_food),
                         (x, y, config.SIZE_FOOD, config.SIZE_FOOD))


def _draw_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    for unit in config_game.units:
        x, y = config_game.units_coordinates[config_game.units.index(unit)][0], \
               config_game.units_coordinates[config_game.units.index(unit)][1]
        color_unit = config.GREEN_1
        pygame.draw.rect(WINDOW, color_unit, (x, y, config.SIZE_UNIT, config.SIZE_UNIT))
        for food in config_game.food:
            if x <= food[0] <= x + config.SIZE_UNIT:
                if y <= food[1] <= y + config.SIZE_UNIT:
                    config_game.units_for_duplicate[config_game.units.index(unit)] += config.ENERGY_FOOD
                    config_game.food.remove(food)
                    for food_second in config_game.units_for_food:
                        if food_second == food:
                            config_game.units_for_food[config_game.units_for_food.index(food_second)] = [None, None]
        # del config_game.units_for_food[unit][1]
        # config_game.units_for_food.clear()


def _draw_radius_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    for unit in config_game.units:
        x = config_game.units_coordinates[config_game.units.index(unit)][0] + config.SIZE_UNIT / 2
        y = config_game.units_coordinates[config_game.units.index(unit)][1] + config.SIZE_UNIT / 2
        color_unit = unit
        SIZE_RADIUS = config.SIZE_UNIT * config_game.unit_genes[config_game.units.index(unit)][4]
        x_start_radius, y_start_radius = x - SIZE_RADIUS / 2, y - SIZE_RADIUS / 2
        x_end_radius, y_end_radius = x_start_radius + SIZE_RADIUS, y_start_radius + SIZE_RADIUS

        food_coord = []
        for food in config_game.food:
            if x_start_radius < food[0] < x_end_radius:
                if y_start_radius < food[1] < y_end_radius:
                    food_coord.append(food)
        #
        # for x_d in range(int(x_start_radius), int(x_end_radius)):
        #     for y_d in range(int(y_start_radius), int(y_end_radius)):
        #         if [x_d, y_d] in config_game.food:
        #             food_coord.append([x_d, y_d])

        # print(food_coord)
        if len(food_coord) != 0:
            food_insert = random.choice(food_coord)
            if food_insert not in config_game.units_for_food:
                if config_game.units_for_food[config_game.units.index(unit)] == [None, None]:
                    config_game.units_for_food[config_game.units.index(unit)] = food_insert

        if config.DRAW_RADIUS:
            pygame.draw.rect(WINDOW, (color_unit),
                             (x_start_radius, y_start_radius,
                              SIZE_RADIUS, SIZE_RADIUS),
                             1)


def _moving_unit(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    for unit in config_game.units:
        x_now = config_game.units_coordinates[config_game.units.index(unit)][0]
        y_now = config_game.units_coordinates[config_game.units.index(unit)][1]
        plus_x, plus_y = 0, 0
        if config_game.units_for_food[config_game.units.index(unit)] != [None, None]:
            x_food = config_game.units_for_food[config_game.units.index(unit)][0]
            y_food = config_game.units_for_food[config_game.units.index(unit)][1]

            if x_food - x_now <= 0:
                plus_x = -config_game.unit_genes[config_game.units.index(unit)][4]
            if y_food - y_now <= 0:
                plus_y = -config_game.unit_genes[config_game.units.index(unit)][4]
            if x_food - (x_now + config.SIZE_UNIT) >= 0:
                plus_x = config_game.unit_genes[config_game.units.index(unit)][4]
            if y_food - (y_now + config.SIZE_UNIT) >= 0:
                plus_y = config_game.unit_genes[config_game.units.index(unit)][4]
        else:
            dec_left, dec_right, dec_up, dec_down, dec_stop = config_game.unit_genes[config_game.units.index(unit)][0], \
                                                              config_game.unit_genes[config_game.units.index(unit)][1], \
                                                              config_game.unit_genes[config_game.units.index(unit)][2], \
                                                              config_game.unit_genes[config_game.units.index(unit)][3], \
                                                              config_game.unit_genes[config_game.units.index(unit)][8]
            speed_unit = config_game.unit_genes[config_game.units.index(unit)][4]

            x_dec = random.choices(['left', 'right', 'stop'], weights=[dec_left, dec_right, dec_stop], k=1)[0]
            y_dec = random.choices(['up', 'down', 'stop'], weights=[dec_up, dec_down, dec_stop], k=1)[0]
            if x_dec == 'left':
                plus_x = -random.randint(1, speed_unit)
            elif x_dec == 'right':
                plus_x = random.randint(1, speed_unit)
            elif x_dec == 'stop':
                plus_x = 0
            if y_dec == 'up':
                plus_y = -random.randint(1, speed_unit)
            elif y_dec == 'down':
                plus_y = random.randint(1, speed_unit)
            elif y_dec == 'stop':
                plus_y = 0

        config_game.units_coordinates[config_game.units.index(unit)][0] += plus_x
        config_game.units_coordinates[config_game.units.index(unit)][1] += plus_y

        x_now = config_game.units_coordinates[config_game.units.index(unit)][0]
        y_now = config_game.units_coordinates[config_game.units.index(unit)][1]
        if x_now + config.SIZE_UNIT + 1 > WINDOW_WIDTH:  # справа край экрана
            # print(f'[{x_now},{y_now}] - {WINDOW_START}-{WINDOW_WIDTH} | 0 - {WINDOW_HEIGHT}')
            config_game.units_coordinates[config_game.units.index(unit)] = [int(WINDOW_START), y_now]
                # x_dec = random.choices(['left', 'stop'], weights=[dec_left, dec_stop], k=1)[0]
                # if x_dec == 'left':
                #     plus_x = -random.randint(1, speed_unit)
                # elif x_dec == 'stop':
                #     plus_x = 0
        elif x_now - config.SIZE_UNIT < WINDOW_START:  # слева край экрана
            # print(f'[{x_now},{y_now}] - {WINDOW_START}-{WINDOW_WIDTH} | 0 - {WINDOW_HEIGHT}')
            config_game.units_coordinates[config_game.units.index(unit)] = [int(WINDOW_WIDTH-config.SIZE_UNIT), y_now]
            #     x_dec = random.choices(['right', 'stop'], weights=[dec_right, dec_stop], k=1)[0]
            #     if x_dec == 'right':
            #         plus_x = random.randint(1, speed_unit)
            #     elif x_dec == 'stop':
            #         plus_x = 0
        elif y_now - config.SIZE_UNIT < 0:  # верх край экрана
            # print(f'[{x_now},{y_now}] - {WINDOW_START}-{WINDOW_WIDTH} | 0 - {WINDOW_HEIGHT}')
            config_game.units_coordinates[config_game.units.index(unit)] = [x_now, int(WINDOW_HEIGHT)-config.SIZE_UNIT]
            #     y_dec = random.choices(['down', 'stop'], weights=[dec_down, dec_stop], k=1)[0]
            #     if y_dec == 'down':
            #         plus_y = random.randint(1, speed_unit)
            #     elif y_dec == 'stop':
            #         plus_y = 0
        elif y_now + config.SIZE_UNIT > WINDOW_HEIGHT:  # низ, край экрана
            # print(f'[{x_now},{y_now}] - {WINDOW_START}-{WINDOW_WIDTH} | 0 - {WINDOW_HEIGHT}')
            config_game.units_coordinates[config_game.units.index(unit)] = [x_now, 0]
            #     y_dec = random.choices(['up', 'stop'], weights=[dec_up, dec_stop], k=1)[0]
            #     if y_dec == 'up':
            #         plus_y = -random.randint(1, speed_unit)
            #     elif y_dec == 'stop':
            #         plus_y = 0


def _spawn_food_every_time(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    if config_game.time_step >= config.ONE_YEAR:
        for food in range(config.SPAWN_FOOD):
            x = random.randint(WINDOW_START, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            color_food = config.RED_1
            pygame.draw.rect(WINDOW, (color_food),
                             (x, y, config.SIZE_FOOD, config.SIZE_FOOD))

            config_game.food.append([x, y])


def _spawn_duplicate(WINDOW, unit, x, y):
    color_unit = random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000)
    pygame.draw.rect(WINDOW, (config.GREEN_1),
                     (x, y, config.SIZE_UNIT, config.SIZE_UNIT))

    _insert_unit(color_unit, x, y, unit)


def _duplicate(WINDOW):
    for unit in config_game.units:
        index_unit = config_game.units.index(unit)

        x = config_game.units_coordinates[index_unit][0]
        y = config_game.units_coordinates[index_unit][1]

        duplicate = config_game.units_for_duplicate[index_unit]
        if duplicate >= config.FOOD_FOR_DUPLICATE:
            for_yeah = config_game.unit_genes[index_unit][6]
            result = random.choices([True, False], weights=[for_yeah, 100 - for_yeah], k=1)[0]
            if result is True:
                _spawn_duplicate(WINDOW, unit, x, y)
                config_game.units_for_duplicate[config_game.units.index(unit)] -= config.FOOD_FOR_DUPLICATE


def _plus_life(WINDOW):
    for unit in config_game.units:
        index_unit = config_game.units.index(unit)
        duplicate = config_game.units_for_duplicate[index_unit]
        if duplicate >= config.FOOD_FOR_PLUS_LIFE:
            for_yeah = config_game.unit_genes[index_unit][7]
            result = random.choices([True, False], weights=[for_yeah, 100 - for_yeah], k=1)[0]
            if result is True:
                print('Ктото увеличил себе жизнь')
                config_game.units_for_duplicate[config_game.units.index(unit)] -= config.FOOD_FOR_PLUS_LIFE
                config_game.units_life[config_game.units.index(unit)] -= config.PLUS_LIFE_AFTER


def _food_after_dead(WINDOW):
    for unit in config_game.units:
        index_unit = config_game.units.index(unit)
        len_life = config_game.units_life[index_unit]
        if len_life > config.LEN_LIFE:
            x_for_food = config_game.units_coordinates[index_unit][0]
            y_for_food = config_game.units_coordinates[index_unit][1]

            for_range = config_game.units_for_duplicate[config_game.units.index(unit)]
            color_food = config.RED_1

            for plus_food in range(for_range):
                x = random.randint(x_for_food, x_for_food + config.SIZE_UNIT)
                y = random.randint(y_for_food, y_for_food + config.SIZE_UNIT)
                if [x, y] not in config_game.food:
                    config_game.food.append([x, y])
                    pygame.draw.rect(WINDOW, (color_food),
                                     (x, y, config.SIZE_FOOD, config.SIZE_FOOD))
            _delete_unit(unit)


def dominant_gen():
    lll = []
    for gens in config_game.unit_genes:
        in_lll = ''
        for gen in gens:
            in_lll += f'{gen} '
        lll.append(in_lll)
    my_dict = Counter(lll)
    print(my_dict)


def _zero_step():
    if config_game.time_step >= config.ONE_YEAR:
        config_game.now_year += 1
        config_game.time_step = 0
        config_game.now_mouth = 0
        dominant_gen()
    if config_game.time_step >= config.ONE_YEAR / 12 * config_game.now_mouth:
        config_game.now_mouth += 1
        for unit in config_game.units:
            config_game.units_life[config_game.units.index(unit)] += 1

        # if config_game.now_mouth == 11 and int(config.ONE_YEAR / 12 * 11) >= config_game.time_step:
        #     config_game.now_mouth = 12
