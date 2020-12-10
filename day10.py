#!/usr/bin/env python

with open("day10.input.txt") as f:
    adapters = sorted(int(x.strip()) for x in f)
    assert len(set(adapters)) == len(adapters)

def run():
    count_1 = 1  # pre-counted: outlet -> adapter
    count_3 = 1  # pre-counted: adapter -> phone

    for b, c in zip(adapters, adapters[1:]):
        assert 0 <= c - b <= 3, (b, c)

        if c - b == 3:
            count_3 += 1

        if c - b == 1:
            count_1 += 1

    return count_1 * count_3

part1 = run()

print("part 1: {}".format(run()))
