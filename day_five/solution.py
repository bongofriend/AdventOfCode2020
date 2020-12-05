from os import path
from itertools import combinations

def read_seats():
    current_dir = path.dirname(path.abspath(__file__))
    with open(path.join(current_dir, "seats.txt"), "r") as f:
        seats = [l.rstrip() for l in f.readlines()]
    return seats


def binary_partition(data: str, start: int, end: str, lower_char: str, upper_char: str) -> int:
    lower = start
    upper = end
    for c in data:
        if c == upper_char:
            lower = int((upper + lower) / 2)
        elif c == lower_char:
            upper = int((upper + lower) / 2)
    return upper

def get_seat_position(seat: str) -> list:
    row = binary_partition(seat[0:7], 0, 127, "F", "B")
    row_pos = binary_partition(seat[7:10], 0, 7, "L", "R")
    return (row * 8) + row_pos

def solution_1():
    seats = read_seats()
    data = [get_seat_position(s) for s in seats]
    max_seat = max(data)
    return max_seat

def solution_2():
    seats = read_seats()
    data = [get_seat_position(s) for s in seats]
    data.sort()
    for a, b in zip(data, data[1:]):
        if b - a == 2:
            return str(a + 1)

        
print(solution_2())