def seat_id(line):
    return int(
        line.strip()
        .replace("F", "0")
        .replace("B", "1")
        .replace("R", "1")
        .replace("L", "0"),
        2
    )

with open("day5.input.txt") as f:
    seat_ids = sorted(map(seat_id, f))

print("part 1: {}".format(max(seat_ids)))
print("part 2: {}".format(next(a + 1 for a, b in zip(seat_ids, seat_ids[1:]) if a == b - 2)))
