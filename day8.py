import os
import sys
import math

def part1():
    with open(os.path.join(sys.path[0], 'day8.txt'), 'r') as file:
        lines = file.read().strip().splitlines()

        steps = 0
        path = lines[0]
        lines = lines[2:]
        next_step = 'AAA'
        while next_step != 'ZZZ':
            i = 0
            for i in range(len(lines)):
                if(lines[i][0:3] == next_step):
                    if(path[steps % len(path)] == 'L'):
                        next_step = lines[i][7:10]
                    if(path[steps % len(path)] == 'R'):
                        next_step = lines[i][12:15]
                    steps += 1
                if(next_step == 'ZZZ'):
                    break
        print(steps)

def part2():
    with open(os.path.join(sys.path[0], 'day8.txt'), 'r') as file:
        lines = file.read().strip().splitlines()

    steps = []
    path = lines[0]
    lines = lines[2:]
    next_steps = []
    for line in lines:
        if(line[2] == 'A'):
            next_steps.append(line[0:3])


    for next_step in next_steps:
        current_steps = 0
        while next_step[2] != 'Z':
            i = 0
            for i in range(len(lines)):
                if (lines[i][0:3] == next_step):
                    if (path[current_steps % len(path)] == 'L'):
                        next_step = lines[i][7:10]
                    if (path[current_steps % len(path)] == 'R'):
                        next_step = lines[i][12:15]
                    current_steps += 1
                if (next_step[2] == 'Z'):
                    steps.append(current_steps)
                    break
    print(math.lcm(*steps))


if __name__ == '__main__':
    part1()
    part2()