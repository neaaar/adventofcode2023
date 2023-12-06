import os
import sys
import re

def part1():
    with open(os.path.join(sys.path[0], 'day6.txt'), 'r') as file:
        data = file.read().splitlines()
        
        time = map(int, re.findall('\d+', data[0]))
        distance = map(int, re.findall('\d+', data[1]))

        res = 1
        for i in range(len(time)):
            count = 0
            for j in range(time[i]):
                charge_time = time[i] - j
                movement_time = time[i] - charge_time

                if charge_time * movement_time > distance[i]:
                    count += 1
            if(count > 0):
                res *= count
    print(res)

def part2():
    with open(os.path.join(sys.path[0], 'day6.txt'), 'r') as file:
        data = file.read().splitlines()
        
        time_chunks = re.findall('\d+', data[0])
        time = ''
        for i in time_chunks:
            time += i
        time = int(time)

        distance_chunks = re.findall('\d+', data[1])
        distance = ''
        for i in distance_chunks:
            distance += i
        distance = int(distance)

        count = 0
        for i in range(time):
            charge_time = time - i
            movement_time = time - charge_time

            if charge_time * movement_time > distance:
                count += 1
        print(count)




if __name__== '__main__':
    part1()
    part2()