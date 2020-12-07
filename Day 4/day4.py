def has_required_fields(keys: list):
    required_keys = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
        ]
    return all(key in keys for key in required_keys)

with open("input.txt") as input_file:
    values = [p.split() for p in input_file.read().split("\n\n")]
    passports = [dict(pair.split(":") for pair in passport) for passport in values]

validated_passports = [has_required_fields(passport) for passport in passports]
print(validated_passports.count(True))