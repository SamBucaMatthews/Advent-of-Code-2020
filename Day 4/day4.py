import re

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

def has_valid_fields(fields: dict):
    if int(fields.get("byr")) < 1920 or int(fields.get("byr")) > 2002:
        return False
    
    if int(fields.get("iyr")) < 2010 or int(fields.get("iyr")) > 2020:
        return False

    if int(fields.get("eyr")) < 2020 or int(fields.get("eyr")) > 2030:
        return False

    # TODO: Height

    if not re.fullmatch("#[0-9a-zA-Z]{6}", fields.get("hcl")):
        return False

    return True      

def is_valid(passport: dict):
    return has_required_fields(passport.keys()) and has_valid_fields(passport)    

with open("input.txt") as input_file:
    values = [p.split() for p in input_file.read().split("\n\n")]
    passports = [dict(pair.split(":") for pair in passport) for passport in values]

validated_passports = [is_valid(passport) for passport in passports]
print(validated_passports.count(True))