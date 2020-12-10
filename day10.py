#!/usr/bin/env python

with open("day10.input.txt") as f:
    adapters = sorted(int(x.strip()) for x in f)
    assert len(set(adapters)) == len(adapters)

def run():
    count_1 = 0
    count_3 = 1  # pre-counted: adapter -> phone

    # solution to part 2 -- we start out with 1 combination and multiply by 2
    # every time we try to omit an adapter
    combinations = 1
    jolt_1_len = 0  # current streak of 1-jolt differences
    a = 0
    for b in adapters:
        jolt = b - a

        if jolt == 3:
            jolt_1_len = 0
            count_3 += 1

        elif jolt == 1:
            jolt_1_len += 1
            count_1 += 1

            if 1 < jolt_1_len < 4:
                # a length-n sequence of 1-jolt increments can generally have
                # all but the last adapter omitted: 2 ^ (n-1)
                combinations *= 2
            elif jolt_1_len == 4:
                # length-4 jolt groups cannot have all three adapters omitted
                # at the same time:
                # 2 ^ (n-1) - 1 = 7
                #
                # unfortunately we only have a single integer so we need to
                # undo a bit of previous calculation
                combinations /= 4
                combinations *= 7
        else:
            assert False, (a, b)

        a = b

    return count_1 * count_3, combinations

part1, part2 = run()

print("part 1: {}".format(part1))
print("part 2: {}".format(part2))
