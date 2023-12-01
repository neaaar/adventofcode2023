import os
import sys
import re

def part1():
    sum = 0
    with open(os.path.join(sys.path[0], 'day1.txt'), 'r') as file:
        data = file.read().splitlines()

        for line in data:
            n = re.findall(r'\d' , line)
            sum += int(n[0] + n[-1])

    print(sum)

def part2():
    values = {
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
        'zero' : '0'
    }

    sum = 0
    with open(os.path.join(sys.path[0], 'day1.txt'), 'r') as file:
        data = file.read().splitlines()

        for line in data:
            words = re.findall("(?=(" + "|".join(values.keys()) + "|\d))" , line)
            sum += int(''.join(d if d.isdigit() else values[d] for d in (words[0], words[-1])))

    print(sum)

if __name__ == "__main__":
    part1()
    part2()