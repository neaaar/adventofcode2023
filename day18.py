import os
import sys

def part1():
    with open(os.path.join(sys.path[0], 'day18.txt'), 'r') as file:
        lines = file.read().strip().splitlines()
    
    vertices = []
    current = (0, 0)
    last_dir = ''
    edges = 0
    for line in lines:
        dir, count, hex = line.split(' ')
        count = int(count)
        edges += count

        if dir == 'U':
            x, y = current
            current = (x, y + count)
        if dir == 'R':
            x, y = current
            current = (x + count, y)
        if dir == 'D':
            x, y = current
            current = (x, y - count)
        if dir == 'L':
            x, y = current
            current = (x - count, y)

        if dir != last_dir:
            vertices.append(current)
        last_dir = dir
    
    sum1 = 0
    sum2 = 0
    for i in range(len(vertices) - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]

        sum1 += x1 * y2
        sum2 += y1 * x2
    
    print(int(abs(sum1 - sum2) / 2 + edges / 2 + 1))

def part2():
    with open(os.path.join(sys.path[0], 'day18.txt'), 'r') as file:
        lines = file.read().strip().splitlines()
    
    vertices = []
    current = (0, 0)
    last_dir = ''
    edges = 0
    for line in lines:
        hex = line.split(' ')[2][2:-1]
        
        count = int(hex[0:-1], 16)
        dir = hex[-1]
        edges += count

        if dir == '3':
            x, y = current
            current = (x, y + count)
        if dir == '0':
            x, y = current
            current = (x + count, y)
        if dir == '1':
            x, y = current
            current = (x, y - count)
        if dir == '2':
            x, y = current
            current = (x - count, y)

        if dir != last_dir:
            vertices.append(current)
        last_dir = dir
    
    sum1 = 0
    sum2 = 0
    for i in range(len(vertices) - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]

        sum1 += x1 * y2
        sum2 += y1 * x2
    
    print(int(abs(sum1 - sum2) / 2 + edges / 2 + 1))


if __name__ == '__main__':
    part1()
    part2()
