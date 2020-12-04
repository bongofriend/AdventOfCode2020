from os import path
import string

valid_passport_fields = set(["ecl", "pid", "eyr", "hcl", "byr", "iyr", "cid", "hgt"])


passport_validators = {
    "byr": lambda p: valid_year(p, "byr", 1920, 2002),
    "iyr": lambda p: valid_year(p, "iyr", 2010, 2020),
    "eyr": lambda p: valid_year(p, "eyr", 2020, 2030),
    "hgt": lambda p: valid_height(p),
    "hcl": lambda p: valid_hair_color(p),
    "ecl": lambda p: p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda p: valid_pid(p)
}

def valid_year(p: dict, key: str, lower: int, upper: int) -> bool:
    y = int(p[key])
    return len(p[key]) == 4 and y >= lower and y <= upper

def valid_height(p: dict):
    h: str = p["hgt"]
    if "cm" in h:
        n = int(h.replace("cm", ""))
        return n >= 150 and n <= 193
    elif "in" in h:
        n = int(h.replace("in", ""))
        return n >= 59 and n <= 76
    else:
        return False

def valid_hair_color(p: dict) -> bool:
    h: str = p["hcl"]
    d = h[1:]
    return h[0] == "#" and set(d).issubset(string.hexdigits)

def valid_pid(p: dict) -> bool:
    i: str = p["pid"]
    return len(i) == 9 and i.isnumeric()

def process_passport_data(lines):
    passport = dict()
    for l in lines:
        data = l.split(" ")
        for d in data:
            [key, value] = d.split(":")
            passport[key] = value
    return passport

def read_passports():
    passports = list()
    current_dir = path.dirname(path.abspath(__file__))
    with open(path.join(current_dir, "passports.txt"), "r") as f:
        lines = [l.rstrip() for l in f.readlines()]
        current_passport_data = list()
        for line in lines:
            if line == "":
                passports.append(process_passport_data(current_passport_data))
                current_passport_data.clear()
            else:
                current_passport_data.append(line)
    if len(current_passport_data) > 0:
        passports.append(process_passport_data(current_passport_data))
    return passports


def is_valid(passport: dict):
    keys = set(passport.keys())
    valid_fields = set(valid_passport_fields)
    north_pole = valid_fields.copy()
    north_pole.remove("cid")
    return keys == valid_fields or keys == north_pole

def is_valid_by_content(p: dict) -> bool:
    for key, validator in passport_validators.items():
        if not validator(p):
            return False
    return True

def solution_1():
    passports = read_passports()
    print(len(list(filter(lambda p: is_valid(p), passports))))

def solution_2():
    passports = read_passports()
    valid_passports = list(filter(lambda p: is_valid(p), passports))
    valid_passports_by_content = list(filter(lambda p: is_valid_by_content(p), valid_passports))
    return len(valid_passports_by_content)
