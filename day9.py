#!/usr/bin/env python
from collections import deque

PREAMBLE_LEN = 25

def run_part1(numbers):
    # store last n numbers for lookup by value
    last_n_set = set()
    # store last n numbers for knowing in which order to truncate
    last_n = deque()

    for number in numbers:
        if len(last_n) > PREAMBLE_LEN:
            to_remove = last_n.popleft()
            last_n_set.remove(to_remove)
            assert len(last_n) == PREAMBLE_LEN

        if (
            len(last_n) == PREAMBLE_LEN and
            not any(number - number2 in last_n_set for number2 in last_n_set)
        ):
            return number

        last_n.append(number)
        last_n_set.add(number)

        # assumption about input: within the last n numbers no number appears twice
        assert len(last_n_set) == len(last_n)

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
