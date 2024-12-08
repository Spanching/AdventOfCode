
from collections import defaultdict


def task1(puzzle_input: list[str]) -> int:
    antinodes = []
    antennas = extract_antennas(puzzle_input)
    n, m = len(puzzle_input), len(puzzle_input[0])
    for key in antennas:
        for idx, (x1, y1) in enumerate(antennas[key]):
            if idx == len(antennas[key]) - 1:
                continue
            for (x2, y2) in antennas[key][idx+1:]:
                delta_x = x1 - x2
                delta_y = y1 - y2
                antinode_1 = (x1 + delta_x, y1 + delta_y)
                antinode_2 = (x2 - delta_x, y2 - delta_y)
                add_if_in_bounds(antinodes, n, m, antinode_1)
                add_if_in_bounds(antinodes, n, m, antinode_2)
    return len((antinodes))

def add_if_in_bounds(antinodes, n, m, antinode):
    if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < n and antinode[1] < m:
        antinodes.append(antinode)
        return True
    return False

def task2(puzzle_input: list[str]) -> int:
    antinodes = []
    antennas = extract_antennas(puzzle_input)
    n, m = len(puzzle_input), len(puzzle_input[0])
    for key in antennas:
        for idx, (x1, y1) in enumerate(antennas[key]):
            if idx == len(antennas[key]) - 1:
                continue
            for (x2, y2) in antennas[key][idx+1:]:
                delta_x = x1 - x2
                delta_y = y1 - y2
                count = 0
                while True:
                    antinode_1 = (x1 + count*delta_x, y1 + count*delta_y)
                    if not add_if_in_bounds(antinodes, n, m, antinode_1):
                        break
                    count += 1
                count = 0
                while True:
                    antinode_2 = (x2 - count*delta_x, y2 - count*delta_y)
                    if not add_if_in_bounds(antinodes, n, m, antinode_2):
                        break
                    count += 1
    for antinode in antinodes:
        puzzle_input[antinode[0]] = puzzle_input[antinode[0]][0:antinode[1]] + "#" + puzzle_input[antinode[0]][antinode[1]+1:]
    return len(set(antinodes))

def extract_antennas(puzzle_input):
    antennas = defaultdict(list)
    for i, line in enumerate(puzzle_input):
        for j, c in enumerate(line):
            if c == '.':
                continue
            else:
                antennas[c].append((i, j))
    return antennas

