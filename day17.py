import os
import sys
from queue import PriorityQueue

def least_heat(grid, height, width, minimum_streak, maximum_streak):
    frontier = PriorityQueue()
    frontier.put((grid[(1, 0)], (1, 0), (1, 0), 0))
    frontier.put((grid[(0, 1)], (0, 1), (0, 1), 0))
    visited = set()
    target = (width - 1, height - 1)
    while not frontier.empty():
        cost, (x, y), (dx, dy), streak = frontier.get()
        if (x, y) == target and minimum_streak <= streak:
            return cost
        if ((x, y), (dx, dy), streak) in visited:
            continue
        visited.add(((x, y), (dx, dy), streak))
        if streak < (maximum_streak - 1) and (x + dx, y + dy) in grid:
            straight_position = (x + dx, y + dy)
            straight_cost = cost + grid[straight_position]
            frontier.put((straight_cost, straight_position, (dx, dy), streak + 1))
        if streak >= minimum_streak:
            lx, ly = dy, -dx
            left_position = (x + lx, y + ly)
            rx, ry = -dy, dx
            right_position = (x + rx, y + ry)
            if left_position in grid:
                left_cost = cost + grid[left_position]
                frontier.put((left_cost, left_position, (lx, ly), 0))
            if right_position in grid:
                right_cost = cost + grid[right_position]
                frontier.put((right_cost, right_position, (rx, ry), 0))

def part1():
    with open(os.path.join(sys.path[0], 'day17.txt'), 'r') as file:
        data = file.read().strip().splitlines()
    
    height, width = len(data), len(data[0])
    grid = {(x, y): int(n) for y, line in enumerate(data) for x, n in enumerate(line)}

    print(least_heat(grid, height, width, 0, 3))


def part2():
    with open(os.path.join(sys.path[0], 'day17.txt'), 'r') as file:
        data = file.read().strip().splitlines()

    height, width = len(data), len(data[0])
    grid = {(x, y): int(n) for y, line in enumerate(data) for x, n in enumerate(line)}

    print(least_heat(grid, height, width, 3, 10))

    

if __name__ == '__main__':
    part1()
    part2()