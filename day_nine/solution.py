from os import path
from itertools import combinations

def verfiy(data: list[int], preamble_size: int = 25) -> int:
    for i in range(preamble_size, len(data)):
        lower = i - preamble_size
        uppper = i
        preamble = data[lower:uppper]
        found = False
        for d in combinations(preamble, 2):
            if sum(d) == data[i]:
                found =  True
        if not found:
            return data[i]

def add_upp(target: int, data: list[int]) -> int:
    for lower in range(len(data)):
        upper = lower
        i = 2
        while upper + i < len(data) and sum(data[lower:upper+i]) != target:
            i += 1
        r = data[lower:upper+i]
        if sum(r) == target:
            return min(r) + max(r)
    return -2



d = path.dirname(path.abspath(__file__))
with open(path.join(d, 'input.txt')) as f:
    data = [int(l.rstrip()) for l in f.readlines()]
    invalid = verfiy(data, 25)
    print(add_upp(invalid, data))