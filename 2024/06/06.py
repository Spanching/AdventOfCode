
from typing import Tuple

from tqdm import tqdm

directions = {
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1)   
}

def guard_position(level: list[str]) -> Tuple[int, int, chr]:
    for i, line in enumerate(level):
        for direction in directions:
            if direction in line:
                return (i, line.index(direction), direction)

def run(level: list[str], i, j, direction):
    visited = []
    deltay, deltax = directions[direction]
    while i!=0 and i!=len(level)-1 and j!=0 and j!=len(level[0])-1:
        if level[i+deltay][j+deltax] == '#':
            # turn to right
            direction_list = list(directions)
            direction = direction_list[(direction_list.index(direction)+1) % 4]
            deltay, deltax = directions[direction]
        else:
            if (i,j) not in visited:
                visited.append((i,j))
            i += deltay
            j += deltax
    return len(set(visited)) + 1

def positions(level: list[str], i, j, direction) -> list[tuple[int, int, chr]]:
    visited = []
    y, x = i, j
    deltay, deltax = directions[direction]
    while y!=0 and y!=len(level)-1 and x!=0 and x!=len(level[0])-1:
        if level[y+deltay][x+deltax] == '#':
            # turn to right
            direction_list = list(directions)
            direction = direction_list[(direction_list.index(direction)+1) % 4]
            deltay, deltax = directions[direction]
        else:
            y += deltay
            x += deltax
            if (y,x) not in visited:
                visited.append((y,x))
    return visited

def is_cycle(level: list[str], i, j, direction):
    visited = []
    deltay, deltax = directions[direction]
    while i!=0 and i!=len(level)-1 and j!=0 and j!=len(level[0])-1:
        if level[i+deltay][j+deltax] == '#':
            # turn to right
            direction_list = list(directions)
            direction = direction_list[(direction_list.index(direction)+1) % 4]
            deltay, deltax = directions[direction]
        else:
            if (i,j, direction) in visited:
                return True
            visited.append((i,j, direction))
            i += deltay
            j += deltax
    return False

def customize_level(level: list[str], i, j) -> list[str]:
    new_level = list.copy(level)
    new_level[i] = level[i][:j] + '#' + level[i][j+1:]
    return new_level

def task1(level: list[str]) -> int:
    i, j, direction = guard_position(level)
    return run(level, i, j, direction)

def task2(level: list[str]) -> int:
    sum = 0
    i, j, direction = guard_position(level)
    for (y, x) in tqdm(positions(level, i, j, direction)):
        if y==i and x==j:
            continue
        new_level = customize_level(level, y, x)
        if is_cycle(new_level, i, j, direction):
            sum += 1
    return sum
