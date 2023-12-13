import os
import sys

def convert_to_row_col(pattern:str):
    pattern = pattern.splitlines()
    h = len(pattern)
    w = len(pattern[0])
    rows = []
    cols = []
    for i in pattern: rows.append(int("".join(map(lambda x: {'#':'1','.':'0'}[x],i)),2))
    for j in range(w): cols.append(int("".join(map(lambda x: {'#':'1','.':'0'}[x],(pattern[i][j] for i in range(h)))),2))
    return rows, cols

def check(a,b):
    A = [x^y for x,y in zip(a,b)]
    A.sort()
    return A[-1] == 0

def find_mirror(hashes:list[int]):
    a = hashes[:: 1]
    b = hashes[::-1]
    n = len(a)
    for i in range(1,n,2):
        if check(a[:i+1], b[n-i-1:]): return (i+1) // 2
        if check(a[n-i-1:], b[:i+1]): return n - (i+1)//2
    return 0

def part1():
    with open(os.path.join(sys.path[0], 'day13.txt'), 'r') as file:
        patterns = file.read().strip().split('\n\n')

    res = 0
    for pattern in patterns:
        row, column = convert_to_row_col(pattern)
        res += 100*find_mirror(row) + find_mirror(column)
    print(res)


def check2(a,b):
    A = [x^y for x,y in zip(a,b)]
    A.sort()
    is_power_of_2 = A[-2]&(A[-2] -1) == 0 and A[-2]
    return is_power_of_2 and (len(A) <= 2 or A[-3] == 0)

def find_mirror2(hashes:list[int]):
    a = hashes[:: 1]
    b = hashes[::-1]
    n = len(a)
    for i in range(1,n,2):
        if check2(a[:i+1], b[n-i-1:]): return (i+1) // 2
        if check2(a[n-i-1:], b[:i+1]): return n - (i+1)//2
    return 0

def part2():
    with open(os.path.join(sys.path[0], 'day13.txt'), 'r') as file:
        patterns = file.read().strip().split('\n\n')

    res = 0
    for pattern in patterns:
        row, column = convert_to_row_col(pattern)
        res += 100*find_mirror2(row) + find_mirror2(column)
    print(res)


if __name__ == '__main__':
    part1()
    part2()