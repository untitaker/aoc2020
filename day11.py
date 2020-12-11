#!/usr/bin/env python
import copy

with open("day11.input.txt") as f:
    seats = list(list(x.strip()) for x in f)


def look(seats, position, direction):
    i, j = position
    a, b = direction

    distance = 0

    while True:
        i += a
        j += b
        distance += 1

        try:
            if j < 0 or i < 0:
                break

            if seats[i][j] == 'L':
                break

            if seats[i][j] == '#':
                return distance
        except IndexError:
            break


def look_around(seats, position, max_distance):
    rv = 0
    for distance in (
        look(seats, position, (-1, -1)),
        look(seats, position, (0, -1)),
        look(seats, position, (1, -1)),

        look(seats, position, (-1, 0)),
        look(seats, position, (1, 0)),

        look(seats, position, (-1, 1)),
        look(seats, position, (0, 1)),
        look(seats, position, (1, 1)),
    ):
        if distance is not None and (max_distance is None or distance <= max_distance):
            rv += 1

    return rv


def run(seats, modifier):
    while True:
        changed = False
        occupied = 0

        new_seats = copy.deepcopy(seats)

        for i, row in enumerate(seats):
            for j, seat in enumerate(row):
                if seat == '#':
                    occupied += 1

                if modifier(seats, new_seats, seat, i, j):
                    changed = True

        if not changed:
            return occupied

        seats = new_seats


def modifier_part1(seats, new_seats, seat, i, j):
    if seat == 'L' and look_around(seats, (i, j), 1) == 0:
        new_seats[i][j] = '#'
        return True
    elif seat == '#' and look_around(seats, (i, j), 1) >= 4:
        new_seats[i][j] = 'L'
        return True


def modifier_part2(seats, new_seats, seat, i, j):
    if seat == 'L' and look_around(seats, (i, j), None) == 0:
        new_seats[i][j] = '#'
        return True
    elif seat == '#' and look_around(seats, (i, j), None) >= 5:
        new_seats[i][j] = 'L'
        return True

part1 = run(seats, modifier_part1)
print("part 1: {}".format(part1))
part2 = run(seats, modifier_part2)
print("part 2: {}".format(part2))
