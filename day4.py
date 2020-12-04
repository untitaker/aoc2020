def run(validators):
    defined_fields = set()
    valid_passports = 0

    with open("day4.input.txt") as f:
        for i, line in enumerate(list(f) + [""]):
            line = line.strip()

            if not line:
                if defined_fields >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
                    valid_passports += 1
                defined_fields = set()

            for word in line.split():
                key, value = word.split(":")
                try:
                    if validators.get(key, lambda _: True)(value):
                        defined_fields.add(key)
                        continue
                except ValueError:
                    pass

                print("Invalid field at line {}: {} is not a valid {}".format(i, value, key))

    return valid_passports


print("{} valid passports, part 1".format(run({})))
print("{} valid passports, part 2".format(run({
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (
        x.endswith("in") and 59 <= int(x[:-2]) <= 76
    ) or (
        x.endswith("cm") and 150 <= int(x[:-2]) <= 193
    ),
    "hcl": lambda x: x[0] == "#" and len(x) == 7 and (int(x[1:], 16) or True),
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: len(x) == 9 and (int(x) or True)
})))
