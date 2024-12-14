from collections import defaultdict
import re
import time
import numpy as np

robot_reg = 'p\=(-?\d*,-?\d*) v\=(-?\d*,-?\d*)'
size = (101,103)

def task1(puzzle_input: list[str]) -> int:
    robots = [ tuple(map(lambda s: complex(*tuple(map(int, s.split(',')))) ,re.match(robot_reg, line).groups())) for line in puzzle_input ]
    positions = []
    quadrants = defaultdict(int)
    for p, v in robots:
        p1 = p + 100*v
        position = (p1.real%size[0], p1.imag%size[1])
        quadrant = 0
        v_half = position[0] // (size[0]//2)
        h_half = position[1] / (size[1]//2) 
        if position[0] / (size[0]//2) < 1:
            pass
        elif position[0] / (size[0]//2) > 1:
            quadrant += 1
        else:
            continue
        if position[1] / (size[1]//2) < 1:
            pass
        elif position[1] / (size[1]//2) > 1:
            quadrant += 2
        else:
            continue
        quadrants[quadrant] += 1
    output = 1
    for amount in quadrants.values():
        output *= amount
    return output

def print_floor(robot_positions):
    for i in range(size[0]):
        for j in range(size[1]):
            if (j,i) in robot_positions:
                print("R", end='')
            else:
                print('.', end='')
        print()
    print()
        

def task2(puzzle_input: list[str]) -> int:
    robots = [ tuple(map(lambda s: complex(*tuple(map(int, s.split(',')))) ,re.match(robot_reg, line).groups())) for line in puzzle_input ]
    for i in range(10000):
        positions = []
        xs = []
        ys = []
        for p, v in robots:
            p1 = p + i*v
            xs.append(p1.real%size[0])
            ys.append(p1.imag%size[1])
            positions.append((p1.real%size[0], p1.imag%size[1]))
        if np.var(xs) < 400 and np.var(ys) < 400:
            print_floor(positions)
            return i
    output = 1
    return output
