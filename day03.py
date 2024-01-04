import sys
import os


def parts1and2():
    with open(os.path.join(sys.path[0], 'day03.txt'), 'r') as file:
        lines = file.readlines()

        res = 0

        rows = len(lines)
        cols = len(lines[0])

        counts = [[0] * cols for _ in range(rows)]
        prods = [[1] * cols for _ in range(rows)]

        for i in range(rows):
            j = 0
            while j < cols:
                ctr = 1
                while j < cols - 1 and lines[i][j].isdigit() and lines[i][j + 1].isdigit():
                    ctr += 1
                    j += 1
                if lines[i][j].isdigit():
                    num = int(lines[i][j - ctr + 1:j + 1])
                    valid = False
                    for x in range(i - 1, i + 2):
                        for y in range(j - ctr, j + 2):
                            if 0 <= x < rows and 0 <= y < cols and lines[x][y] != "." and not lines[x][y].isdigit():
                                valid = True
                            if 0 <= x < rows and 0 <= y < cols and lines[x][y] == "*":
                                counts[x][y] += 1
                                prods[x][y] *= num
                                break
                    if valid:
                        res += num
                j += 1

    ratios = 0

    for i in range(rows):
        for j in range(cols):
            if counts[i][j] == 2:
                ratios += prods[i][j]

    print(res)
    print(ratios)


if __name__ == '__main__':
    parts1and2()
