import sys
import os

def part1():
    with open(os.path.join(sys.path[0], 'day09.txt'), 'r') as file:
        lines = file.read().strip().splitlines()
    
    sum = 0
    for line in lines:
        i = 0
        delta = []
        initial_delta = []
        for number in line.split(' '):
            initial_delta.append(int(number))
        delta.append(initial_delta)

        while delta[i].count(0) != len(delta[i]):
            new_delta = []
            for j in range(len(delta[i])):
                if j == 0:
                    continue
                new_delta.append(delta[i][j] - delta[i][j - 1])
            delta.append(new_delta)
            i += 1

        for j in range(len(delta)):
            new_element = delta[len(delta) - j - 1][-1] + delta[len(delta) - j - 2][-1]
            delta[len(delta) - j - 2].append(new_element)
        sum += new_element
    print(sum)

def part2():
    with open(os.path.join(sys.path[0], 'day09.txt'), 'r') as file:
        lines = file.read().strip().splitlines()

    sum = 0
    for line in lines:
        i = 0
        delta = []
        initial_delta = []
        for number in line.split(' '):
            initial_delta.append(int(number))
        delta.append(initial_delta)

        while delta[i].count(0) != len(delta[i]):
            new_delta = []
            for j in range(len(delta[i])):
                if j == 0:
                    continue
                new_delta.append(delta[i][j] - delta[i][j - 1])
            delta.append(new_delta)
            i += 1

        for j in range(len(delta)):
            new_element = delta[len(delta) - j - 2][0] - delta[len(delta) - j - 1][0]
            delta[len(delta) - j - 2].insert(0, new_element)
        sum += new_element
    print(-sum)


if __name__ == '__main__':
    part1()
    part2()