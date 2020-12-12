#!/usr/bin/env python

from math import radians, cos, sin


def rotate(waypoint, angle):
    x, y = waypoint
    assert angle % 90 == 0
    angle = radians(angle)
    # this float rounding is kind of shit but I still want to use sin/cos :(
    x2 = int(round(x * cos(angle) - y * sin(angle)))
    y2 = int(round(y * cos(angle) + x * sin(angle)))
    return [x2, y2]


def run(instructions, instruction_version=1):
    ship = [0, 0]

    if instruction_version == 2:
        # part 2: waypoint coordinates are relative to the ship because it
        # allows for easier rotation, and because for action F, the waypoint
        # moves with the ship anyway
        waypoint = [10, 1]
    else:
        # part 1: the direction the ship is facing can be thought of as a
        # waypoint with manhattan distance of 1 (relative to ship)
        waypoint = [1, 0]

    to_move = waypoint if instruction_version == 2 else ship

    for action, distance in instructions:
        if action == 'N':
            to_move[1] += distance
        elif action == 'S':
            to_move[1] -= distance
        elif action == 'E':
            to_move[0] += distance
        elif action == 'W':
            to_move[0] -= distance
        elif action == 'L':
            waypoint[:] = rotate(waypoint, distance)
        elif action == 'R':
            waypoint[:] = rotate(waypoint, -distance)
        elif action == 'F':
            ship[0] += waypoint[0] * distance
            ship[1] += waypoint[1] * distance
        else:
            raise ValueError(action)

    return abs(ship[0]) + abs(ship[1])


with open("day12.input.txt") as f:
    instructions = list((line[0], int(line[1:])) for line in f)


print("part 1: {}".format(run(instructions, 1)))
print("part 2: {}".format(run(instructions, 2)))
