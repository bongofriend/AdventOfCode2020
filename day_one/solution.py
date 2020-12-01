from itertools import combinations
from math import prod
from typing import Optional

def find_prod(target: int, num: int) -> int:
    with open('input.txt', 'r') as f:
        data = [int(x.strip()) for x in f.readlines()]
        for c in combinations(data, num):
            if sum(c) == target:
                return prod(c)
    return None
 
print(f"Solution for part 1: {find_prod(2020, 2)}\n")
print(f"Solution for part 2: {find_prod(2020, 3)}")