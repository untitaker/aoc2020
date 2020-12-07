#!/usr/bin/env python

def parse():
    with open("day7.input.txt") as f:
        to_parents = {}
        to_children = {}

        for line in f:
            words = line.strip().split()
            if not words:
                continue

            adjective, base_color, _bags, _contain = words[:4]
            container = adjective, base_color
            containees = words[4:]
            containees_parsed = []

            if containees == ["no", "other", "bags."]:
                containees = []

            while containees:
                containees.pop()  # "bags/bag" + "./,"
                base_color = containees.pop()
                adjective = containees.pop()
                quantity = int(containees.pop())

                containee = adjective, base_color
                containees_parsed.append((quantity, containee))
                to_children.setdefault(container, []).append((quantity, containee))
                to_parents.setdefault(containee, []).append((quantity, container))

    return to_parents, to_children

to_parents, to_children = parse()

def traverse_part1(color):
    rv = {color}

    for _, color2 in to_parents.get(color) or ():
        rv.update(traverse_part1(color2))

    return rv

part1 = traverse_part1(("shiny", "gold"))
part1.remove(("shiny", "gold"))
print(len(part1))

def traverse_part2(color):
    rv = 1

    for quantity, color2 in to_children.get(color) or ():
        rv += quantity * traverse_part2(color2)

    return rv

print(traverse_part2(("shiny", "gold")) - 1)
