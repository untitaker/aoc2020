#!/usr/bin/env python
from collections import deque

PREAMBLE_LEN = 25

def run_part1(numbers):
    for i, number in enumerate(numbers):
        if i >= PREAMBLE_LEN:
            last_n = set(numbers[i - PREAMBLE_LEN:i])

            # Storing last n numbers in a set is an oversimplification of the
            # problem, make sure we at least crash explicitly if that's a wrong
            # assumption. Seems to work so far though.
            assert len(last_n) == PREAMBLE_LEN, "assumption: last n numbers are distinct"

            # We may not sum up a number with itself to reach `number`. If such
            # a number exists in our set it would be half of `number`. Remove
            # from set to make sure it does not count.
            last_n.discard(number / 2.0)

            if not any(number - number2 in last_n for number2 in last_n):
                return number

with open("day9.input.txt") as f:
    numbers = list(int(line.strip()) for line in f)

part1 = run_part1(numbers)
print("part 1: {}".format(part1))

def run_part2(part1, numbers):
    for i, a in enumerate(numbers):
        min_ = a
        max_ = a
        for i in range(i + 1, len(numbers)):
            if a == part1:
                return min_ + max_
            elif a > part1:
                break

            b = numbers[i]
            a += b
            min_ = min((b, min_))
            max_ = max((b, max_))


part2 = run_part2(part1, numbers)
print("part 2: {}".format(part2))
