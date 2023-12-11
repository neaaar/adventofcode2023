import os
import sys
from itertools import combinations

def part1():
    with open(os.path.join(sys.path[0], 'day11.txt'), 'r') as file:
        lines = file.read().strip().splitlines()
    
    empty_rows = [y for y, row in enumerate(lines) if all(x == '.' for x in row)]
    empty_columns = [x for x, column in enumerate(zip(*lines)) if all(y == '.' for y in ''.join(column))]
    galaxies = [(x, y) for x, row in enumerate(lines) for y, value in enumerate(row) if value == '#']
    
    res = 0
    for(g1x, g1y), (g2x, g2y) in combinations(galaxies, 2):
        expansion = 0
        expansion += sum(x in empty_rows for x in range(min(g1x, g2x), max(g1x, g2x)))
        expansion += sum(y in empty_columns for y in range(min(g1y, g2y), max(g1y, g2y)))
        res += abs(g1x - g2x) + abs(g1y - g2y) + expansion
    print(res)

def part2():
    with open(os.path.join(sys.path[0], 'day11.txt'), 'r') as file:
        lines = file.read().strip().splitlines()

    empty_rows = [y for y, row in enumerate(lines) if all(x == '.' for x in row)]
    empty_columns = [x for x, column in enumerate(zip(*lines)) if all(y == '.' for y in ''.join(column))]
    galaxies = [(x, y) for x, row in enumerate(lines) for y, value in enumerate(row) if value == '#']

    res = 0
    for (g1x, g1y), (g2x, g2y) in combinations(galaxies, 2):
        expansion = 0
        expansion += sum(x in empty_rows for x in range(min(g1x, g2x), max(g1x, g2x)))
        expansion += sum(y in empty_columns for y in range(min(g1y, g2y), max(g1y, g2y)))
        res += abs(g1x - g2x) + abs(g1y - g2y) + 999999 * expansion
    print(res)
    


if __name__ == '__main__':
    part1()
    part2()