#!/usr/bin/env python

with open("day8.input.txt") as f:
    instructions = [line.strip().split() for line in f]


def run():
    visited_instructions = set()
    acc = 0
    i = 0

    while i < len(instructions) and i not in visited_instructions:
        visited_instructions.add(i)
        opcode, argument = instructions[i]
        if opcode == 'acc':
            acc += int(argument)
            i += 1
        elif opcode == 'nop':
            i += 1
        elif opcode == 'jmp':
            i += int(argument)
        else:
            raise ValueError(opcode)

    terminated_correctly = i == len(instructions)
    return acc, visited_instructions, terminated_correctly


acc, visited_instructions, terminated_correctly = run()
assert not terminated_correctly
print("part 1: {}".format(acc))


def brute(looping_instructions):
    # I think we only need to brute-force the instructions that have been part
    # of the execution of part 1.
    #
    # Roughly speaking, if there was another instruction outside of
    # looping_instructions that we would have to consider, it would have to be
    # part of a distinct infinite loop that does not share any instructions
    # with part 1. That however would mean that we need to flip at least two
    # instructions.

    for i in looping_instructions:
        opcode, argument = instructions[i]

        if opcode == 'acc':
            continue

        opcode2 = 'nop' if opcode == 'jmp' else 'jmp'
        instructions[i] = opcode2, argument

        acc, visited_instructions, terminated_correctly = run()
        if terminated_correctly:
            return acc

        instructions[i] = opcode, argument

    raise ValueError("No instruction-flip helped")


acc = brute(visited_instructions)
print("part 2: {}".format(acc))
