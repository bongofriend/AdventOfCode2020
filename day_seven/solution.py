from os import path
import re

bag_regex = r"\d\s[a-z]{3,}\s[a-z]{3,}\s"
no_other_regex = r"no\sother\sbags"

def part_1(rules, start_bag):
    bags = [start_bag]
    counter = 0
    while counter < len(bags):
        for line in rules:
            if bags[counter] in line:
                new_bag = ' '.join(line.split()[0:2])
                if new_bag not in bags:
                    bags.append(new_bag)
        counter += 1
    return len(bags) - 1

def part_2(lines: list[str], bag: str) -> int:
    for l in lines:
        e = re.split(r"contains?", l)
        start = e[0]
        end = "".join(e[1:]).strip()
        if bag in start:
            if re.match(no_other_regex, end) is not None:
                return 1
            total = 0
            bags = re.findall(bag_regex, l)
            for b in bags:
                [count, primary, secondary] = [x.rstrip() for x in b.split()]
                total += part_2(lines, f"{primary} {secondary}") * int(count)
            return total + 1





current_dir = path.dirname(path.abspath(__file__))
with open(path.join(current_dir, "rules.txt"), "r") as f:
    lines = [l.rstrip() for l in f.readlines()]
    print(part_1(lines, "shiny gold"))
    print(part_2(lines, "shiny gold") - 1)
