import os
import sys
import re


def part1():
    with open(os.path.join(sys.path[0], 'day05.txt'), 'r') as file:
        data = file.read().split('\n\n')
        seeds = [int(_) for _ in re.findall('\d+', data[0])]

        maps = {}
        query = "([a-z]+-to-[a-z]+)\ map:\n(([0-9\ ]+\n?)+\n?)"
        parsed = re.findall(query, "\n".join(data[1:]))
        for m in parsed:
            maps[m[0]] = list(map(lambda x: list(map(int, x.split())), m[1].strip().splitlines()))

        lowest_location = 999999999
        for seed in seeds:
            current_word = 'seed'
            while current_word != 'location':
                for m in maps:
                    if str(m).startswith(f"{current_word}-to-"):
                        destination_word = re.match(f"{current_word}-to-([a-z]+)", m).groups()[0]
                        for c in maps[m]:
                            if c[1] <= seed <= c[1] + c[2] - 1:
                                destination_number = c[0] + (seed - c[1])
                                break
                            else:
                                destination_number = seed
                    current_word = destination_word
                    seed = destination_number
            if seed < lowest_location:
                lowest_location = seed
        print(lowest_location)

def part2():
    with open(os.path.join(sys.path[0], 'day05.txt'), 'r') as file:
        data = file.read().split('\n\n')
        couples = re.findall('\d+ \d+', data[0])

        seeds = []
        for couple in couples:
            nums = str(couple).split(" ")
            for i in range(int(nums[1])):
                seeds.append(int(nums[0]) + i)

        maps = {}
        query = "([a-z]+-to-[a-z]+)\ map:\n(([0-9\ ]+\n?)+\n?)"
        parsed = re.findall(query, "\n".join(data[1:]))
        for m in parsed:
            maps[m[0]] = list(map(lambda x: list(map(int, x.split())), m[1].strip().splitlines()))

        lowest_location = 999999999
        for seed in seeds:
            current_word = 'seed'
            while current_word != 'location':
                for m in maps:
                    if str(m).startswith(f"{current_word}-to-"):
                        destination_word = re.match(f"{current_word}-to-([a-z]+)", m).groups()[0]
                        for c in maps[m]:
                            if c[1] <= seed <= c[1] + c[2] - 1:
                                destination_number = c[0] + (seed - c[1])
                                break
                            else:
                                destination_number = seed
                    current_word = destination_word
                    seed = destination_number
            if seed < lowest_location:
                lowest_location = seed
        print(lowest_location)


if __name__ == '__main__':
    part1()
    part2()
