import os
import sys

with open(os.path.join(sys.path[0], 'day23.txt'), 'r') as file:
        maze = file.read().strip().splitlines()
    
height = len(maze)
width = len(maze[0])

def dfs(y, x, end_y, end_x, visited, length):
    if y == end_y and x == end_x:
        return length

    if (y, x) in visited:
        return -1

    curr_visited = set(visited)
    curr_visited.add((y, x))

    curr = maze[y][x]

    if curr == "<":
        offsets = [(0, -1)]
    elif curr == ">":
        offsets = [(0, 1)]
    elif curr == "^":
        offsets = [(-1, 0)]
    elif curr == "v":
        offsets = [(1, 0)]
    else:
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    to_visit = []
    for offset in offsets:
        (new_y, new_x) = y + offset[0], x + offset[1]
        if (
            new_y >= 0
            and new_x >= 0
            and new_y < height
            and new_x < width
            and maze[new_y][new_x] != "#"
            and (new_y, new_x) not in curr_visited
        ):
            to_visit.append((new_y, new_x))

    if not to_visit:
        return -1

    return max(
        dfs(
            new_y,
            new_x,
            end_y,
            end_x,
            curr_visited,
            length + 1,
        )
        for (new_y, new_x) in to_visit
    )

def part1():
    sys.setrecursionlimit(10000)
    print(dfs(0, maze[0].index('.'), len(maze) - 1, maze[len(maze) - 1].index('.'), set(), 0))

def compressed_dfs(y, x, end_y, end_x, visited, length):
    if y == end_y and x == end_x:
        return length

    if (y, x) in visited:
        return -1

    visited.add((y, x))

    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    to_visit = []
    for offset in offsets:
        curr_visit = set(visited)
        (new_y, new_x) = y + offset[0], x + offset[1]
        if (
            new_y >= 0
            and new_x >= 0
            and new_y < height
            and new_x < width
            and maze[new_y][new_x] != "#"
            and (new_y, new_x) not in curr_visit
        ):
            run_length = 0
            (cy, cx) = (new_y, new_x)
            while True:
                run_length += 1
                new_coord_neighbours = [
                    (cy + offset[0], cx + offset[1]) for offset in offsets
                ]

                walls = []
                open = []

                for a, b in new_coord_neighbours:
                    if (
                        a >= 0
                        and b >= 0
                        and a < height
                        and b < width
                        and (a, b) not in curr_visit
                    ):
                        if maze[a][b] == "#":
                            walls.append((a, b))
                        else:
                            open.append((a, b))

                if len(open) == 1:
                    curr_visit.add((cy, cx))
                    (cy, cx) = open[0]
                else:
                    break

            to_visit.append(
                (cy, cx, curr_visit, run_length),
            )

    if not to_visit:
        return -1

    return max(
        compressed_dfs(
            new_y,
            new_x,
            end_y,
            end_x,
            curr_visit,
            length + run_length,
        )
        for (new_y, new_x, curr_visit, run_length) in to_visit
    )

def part2():
    sys.setrecursionlimit(10000)
    print(compressed_dfs(0, maze[0].index('.'), len(maze) - 1, maze[len(maze) - 1].index('.'), set(), 0))
    

if __name__ == '__main__':
    part1()
    part2()