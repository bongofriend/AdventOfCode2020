from os import path
from collections import deque

def part_1(adapters: list[int]) -> int:
    jolt_counts = {1: 0, 2: 0, 3: 1}
    adapter_chain = [0]
    current_jolt = 0
    max_jolt = max(adapters)
    while current_jolt < max_jolt:
        possible_adapters = []
        for step in jolt_counts.keys():
            if current_jolt + step in adapters:
                possible_adapters.append([step, current_jolt + step])
                #jolt_counts[step] = jolt_counts[step] + 1
        if len(possible_adapters) == 0:
            break
        min_jolt= min(possible_adapters, key=lambda x: x[1])
        adapter_chain.append(min_jolt[1])
        jolt_counts[min_jolt[0]] = jolt_counts[min_jolt[0]] + 1
        adapters.remove(min_jolt[1])
        current_jolt = min_jolt[1]
    return jolt_counts[1] * jolt_counts[3]


def helper(adapters: set[int], cache: dict[int, int], current_adapter: int, max_jolt: int) -> int:
    if max_jolt == current_adapter:
        return 1
    next_adapters = []
    for s in range(1, 4):
        next_adapter = current_adapter + s
        if next_adapter in adapters:
            next_adapters.append(next_adapter)
    counter = 0
    for n in next_adapters:
        if n in cache:
            count = cache[n]
        else:
            count = helper(adapters, cache, n, max_jolt)
        counter += count
    cache[current_adapter] = counter
    return counter
        
   
def part_2(adapters: list[int]):
    max_jolt = max(adapters)
    adapters = set(adapters)
    cache = dict()
    return helper(adapters, cache, 0, max_jolt)      





current_dir = path.dirname(path.abspath(__file__))
with open(path.join(current_dir, 'input.txt'), 'r') as file:
    adapters = [int(l.rstrip()) for l in file.readlines()]
    print(part_2(adapters))
