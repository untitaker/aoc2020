#!/usr/bin/env python
import string

def run(set_init, func):
    answers = set(set_init)
    answers_count = 0

    with open("day6.input.txt") as f:
        for line in list(f) + [""]:
            line = line.strip()
            if not line:
                answers_count += len(answers)
                answers = set(set_init)
            else:
                func(answers, line)

    return answers_count

print("part 1: {}".format(run("", set.update)))
print("part 2: {}".format(run(string.ascii_lowercase, set.intersection_update)))
