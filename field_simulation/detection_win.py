# СИМУЛЯЦИЯ
import random
import time

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
            _duplicate(WINDOW)


        _zero_step()

        if config_game.units:
            _food_after_dead(WINDOW)


def some_draw(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    x = random.randint(WINDOW_START, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    pygame.draw.rect(WINDOW, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x, y, 10, 10))


def _spawn(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    if config_game.start is False:
        for unit in range(config.SPAWN_FIRST_UNIT):
            x = random.randint(WINDOW_START, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            color_unit = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            pygame.draw.rect(WINDOW, (color_unit),
                             (x, y, config.SIZE_UNIT, config.SIZE_UNIT))

            config_game.units.append(color_unit)
            config_game.units_coordinates.append([x, y])
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
        for unit in config_game.units:
            config_game.units_for_food.append([None, None])
            config_game.units_for_duplicate.append(0)
            config_game.units_life.append(0)
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
        color_unit = unit
        pygame.draw.rect(WINDOW, (color_unit),
                         (x, y, config.SIZE_UNIT, config.SIZE_UNIT))
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
        SIZE_RADIUS = config.SIZE_UNIT * config.RADIUS_UNIT
        x_start_radius, y_start_radius = x - SIZE_RADIUS / 2, y - SIZE_RADIUS / 2
        x_end_radius, y_end_radius = x_start_radius + SIZE_RADIUS, y_start_radius + SIZE_RADIUS

        food_coord = []
        for food in config_game.food:
            if x_start_radius < food[0] < x_end_radius:
                if y_start_radius < food[1] < y_end_radius:
                    food_coord.append(food)
        # print(food_coord)
        if len(food_coord) != 0:
            if config_game.units_for_food[config_game.units.index(unit)] == [None, None]:
                config_game.units_for_food[config_game.units.index(unit)] = random.choice(food_coord)

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
                plus_x = -1
            if y_food - y_now <= 0:
                plus_y = -1
            if x_food - (x_now + config.SIZE_UNIT) >= 0:
                plus_x = 1
            if y_food - (y_now + config.SIZE_UNIT) >= 0:
                plus_y = 1
        else:
            if x_now + config.SIZE_UNIT + 1 > WINDOW_WIDTH:  # справа край экрана
                plus_x = random.randint(-1, 0)
            elif x_now - 1 < WINDOW_START:  # слева край экрана
                plus_x = random.randint(0, 1)
            elif y_now - 1 < 0:  # верх край экрана
                plus_y = random.randint(0, 1)
            elif y_now + config.SIZE_UNIT + 1 > WINDOW_HEIGHT:  # низ, край экрана
                plus_y = random.randint(-1, 0)
            else:
                plus_x = random.randint(-1, 1)
                plus_y = random.randint(-1, 1)
        config_game.units_coordinates[config_game.units.index(unit)][0] += plus_x
        config_game.units_coordinates[config_game.units.index(unit)][1] += plus_y


def _spawn_food_every_time(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_START):
    if config_game.time_step >= config.ONE_YEAR:
        for food in range(config.SPAWN_FOOD):
            x = random.randint(WINDOW_START, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            color_food = config.RED_1
            pygame.draw.rect(WINDOW, (color_food),
                             (x, y, config.SIZE_FOOD, config.SIZE_FOOD))

            config_game.food.append([x, y])


def _spawn_duplicate(WINDOW, x, y):
    color_unit = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    pygame.draw.rect(WINDOW, (color_unit),
                     (x, y, config.SIZE_UNIT, config.SIZE_UNIT))

    config_game.units.append(color_unit)
    config_game.units_coordinates.append([x, y])
    config_game.units_for_duplicate.append(0)
    config_game.units_for_food.append([None, None])
    config_game.units_life.append(0)


def _duplicate(WINDOW):
    for unit in config_game.units:
        index_unit = config_game.units.index(unit)

        x = config_game.units_coordinates[index_unit][0]
        y = config_game.units_coordinates[index_unit][1]

        duplicate = config_game.units_for_duplicate[index_unit]
        if duplicate >= config.FOOD_FOR_DUPLICATE:
            _spawn_duplicate(WINDOW, x, y)
            config_game.units_for_duplicate[config_game.units.index(unit)] = 0


def _food_after_dead(WINDOW):
    for unit in config_game.units:
        index_unit = config_game.units.index(unit)
        len_life = config_game.units_life[index_unit]
        if len_life > config.LEN_LIFE:
            x_for_food = config_game.units_coordinates[index_unit][0]
            y_for_food = config_game.units_coordinates[index_unit][1]

            for_range = config_game.units_for_duplicate[config_game.units.index(unit)]

            config_game.units.remove(unit)
            config_game.units_coordinates.remove(config_game.units_coordinates[index_unit])
            config_game.units_for_food.remove(config_game.units_for_food[index_unit])
            config_game.units_for_duplicate.remove(config_game.units_for_duplicate[index_unit])
            config_game.units_life.remove(config_game.units_life[index_unit])

            color_food = config.RED_1

            for plus_food in range(for_range):
                x = random.randint(x_for_food, x_for_food + config.SIZE_UNIT)
                y = random.randint(y_for_food, y_for_food + config.SIZE_UNIT)
                if [x, y] not in config_game.food:
                    config_game.food.append([x, y])
                    pygame.draw.rect(WINDOW, (color_food),
                                     (x, y, config.SIZE_FOOD, config.SIZE_FOOD))


def _zero_step():
    if config_game.time_step >= config.ONE_YEAR:
        config_game.now_year += 1
        config_game.time_step = 0
        config_game.now_mouth = 0
    if config_game.time_step >= config.ONE_YEAR // 12 * config_game.now_mouth:
        config_game.now_mouth += 1
        for unit in config_game.units:
            config_game.units_life[config_game.units.index(unit)] += 1

        # if config_game.now_mouth == 11 and int(config.ONE_YEAR / 12 * 11) >= config_game.time_step:
        #     config_game.now_mouth = 12
