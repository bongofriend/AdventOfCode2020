from os import path
import math

def search(right: int, down: int) -> int:
    geo_map = []
    current_dir = path.dirname(path.abspath(__file__))
    with open(path.join(current_dir, "input.txt")) as f:
        geo_map = [l.strip() for l in f.readlines()]
    tree_count = 0
    y = 0
    x = 0
    while y < len(geo_map):
        if geo_map[y][x] == "#":
            tree_count += 1
        x = (x + right) % len(geo_map[y])
        y += down
    return tree_count


print(math.prod([
    search(1,1),
    search(3,1),
    search(5,1),
    search(7,1),
    search(1,2)
]))


