import os
import sys
from functools import cache

@cache
def calculate_arrangements(pattern: str, counts: tuple[int]) -> int:
    if not pattern:
        return len(counts) == 0

    if not counts:
        return "#" not in pattern

    result = 0

    if pattern[0] in ".?":
        result += calculate_arrangements(pattern[1:], counts)

    if (
        pattern[0] in "#?"
        and counts[0] <= len(pattern)
        and "." not in pattern[: counts[0]]
        and (counts[0] == len(pattern) or pattern[counts[0]] != "#")
    ):
        result += calculate_arrangements(pattern[counts[0] + 1 :], counts[1:])

    return result

def part1():
    with open(os.path.join(sys.path[0], 'day12.txt'), 'r') as file:
        lines = file.read().strip().splitlines()

    records = []
    for line in lines:
        line = line.strip()
        pattern, counts = line.split()

        counts = tuple(int(x) for x in counts.split(","))

        records.append((pattern, counts))

    total = 0
    for pattern, counts in records:
        total += calculate_arrangements(pattern, counts)
    print(total)

def part2():
    with open(os.path.join(sys.path[0], 'day12.txt'), 'r') as file:
        lines = file.read().strip().splitlines()

    records = []
    for line in lines:
        line = line.strip()
        pattern, counts = line.split()

        pattern = "?".join([pattern] * 5)
        counts = tuple(int(x) for x in counts.split(",")) * 5

        records.append((pattern, counts))

    total = 0
    for pattern, counts in records:
        total += calculate_arrangements(pattern, counts)
    print(total)

if __name__ == '__main__':
    part1()
    part2()