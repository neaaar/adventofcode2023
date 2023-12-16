import os
import sys

with open(os.path.join(sys.path[0], 'day16.txt'), 'r') as file:
    data = file.read().strip().splitlines()

n, m = len(data), len(data[0])
incr = {'R': 1, 'L': -1, 'U':-1j, 'D':1j}

energized = set()
dejavu = set()

def push(start, dir):

    i, j = int(start.imag), int(start.real)
    if not (0 <= i < n and 0 <= j < m):
        return None

    if (start, dir) in dejavu:
        return None

    energized.add(start)
    dejavu.add((start, dir))

    if data[i][j] == '.':
        push(start + incr[dir], dir)

    if data[i][j] == '/':
        match dir:
            case 'R': push(start + incr['U'], 'U')
            case 'L': push(start + incr['D'], 'D')
            case 'U': push(start + incr['R'], 'R')
            case 'D': push(start + incr['L'], 'L')

    if data[i][j] == '\\':
        match dir:
            case 'R': push(start + incr['D'], 'D')
            case 'L': push(start + incr['U'], 'U')
            case 'U': push(start + incr['L'], 'L')
            case 'D': push(start + incr['R'], 'R')

    if data[i][j] == '|':
        match dir:
            case 'R' | 'L':
                push(start + incr['U'], 'U')
                push(start + incr['D'], 'D')
            case 'U' | 'D':
                push(start + incr[dir], dir)

    if data[i][j] == '-':
        match dir:
            case 'R' | 'L':
                push(start + incr[dir], dir)
            case 'U' | 'D':
                push(start + incr['L'], 'L')
                push(start + incr['R'], 'R')



def part1():
    sys.setrecursionlimit(10000)

    push(0 + 0j, 'R')
    print(len(energized))

def part2():
    starts = [(0, 'R'), (0, 'D'), (m, 'L'), (m, 'D'), (0 + (n - 1) * 1j, 'U'), (0 + (n - 1) * 1j, 'R'),
              ((m - 1) + (n - 1) * 1j, 'U'), ((m - 1) + (n - 1) * 1j, 'L')]

    for k in range(1, m - 2):
        starts.append((k, 'D'))
        starts.append((k + (n - 1) * 1j, 'U'))

    for k in range(1, n - 2):
        starts.append((k * 1j, 'R'))
        starts.append(((m - 1) + k * 1j, 'L'))

    return starts


if __name__ == '__main__':
    part1()
    starts = part2()

    res = 0
    for pos, dir in starts:
        energized = set()
        dejavu = set()
        push(pos, dir)
        if len(energized) > res:
            res = len(energized)

    print(res)