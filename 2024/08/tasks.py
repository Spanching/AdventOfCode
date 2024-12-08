
from collections import defaultdict


antennas = defaultdict(list)
antinodes = set()
def task1(puzzle_input: list[str]) -> int:
    for i, line in enumerate(puzzle_input):
        for j, c in enumerate(line):
            if c == '.':
                continue
            else:
                antennas[c].append((i, j))
    for key in antennas:
        for idx, (i, j) in enumerate(antennas[key]):
            if idx == len(antennas[key]) - 1:
                continue
            for (x, y) in antennas[key][idx+1:]:
                print(f"At {(i,j)} and {(x,y)}")
                delta_x = x - i
                delta_y = j - y
                if delta_y < 0:
                    # second is right of first
                    print(i - delta_x, j + delta_y)
                    print(x + delta_x, y - delta_y)
                else:
                    # second is left of first
                    print(i - delta_x, j + delta_y)
                    print(x + delta_x, y - delta_y)
    return 0

def task2(puzzle_input: list[str]) -> int:
    return 0
